#!/usr/bin/env python3

from base64 import decode
from io import BytesIO
from time import time, strptime, mktime, sleep, strftime
from unittest import removeResult
import serial
import pygame
from typing import Dict, List, Optional, Tuple, TextIO
import re
import sys
import selectors
import os
from threading import Thread
from datetime import datetime


COLORS = {
    "white": pygame.Color("#FFFFFF"),
    "platinum": pygame.Color("#E4E4E4"),
    "grey": pygame.Color("#888888"),
    "black": pygame.Color("#222222"),
    "pink": pygame.Color("#FFA7D1"),
    "red": pygame.Color("#E50000"),
    "orange": pygame.Color("#E59500"),
    "brown": pygame.Color("#A06A42"),
    "yellow": pygame.Color("#E5D900"),
    "lime": pygame.Color("#94E044"),
    "green": pygame.Color("#02BE01"),
    "cyan": pygame.Color("#00D3DD"),
    "lblue": pygame.Color("#0083C7"),
    "blue": pygame.Color("#0000EA"),
    "mauve": pygame.Color("#CF6EE4"),
    "purple": pygame.Color("#820080")
}

LOG_FILE = "robotic-place.log"

ADMINS = ["-1359147492"]

SIZE = 100
WIDTH = 100
HEIGHT = 100

PAINT_TIMEOUT = 10

Owner = str
Color = pygame.Color
Tile = Tuple[Color, Owner]


class Board:
    def __init__(self,
                 cols: int,
                 rows: int,
                 default_color: str = "white",
                 default_owner: str = "root"):
        self.cols = cols
        self.rows = rows
        self.board = [[(COLORS[default_color], default_owner)
                       for x in range(cols)] for y in range(rows)]

    def draw(self,
             surface: pygame.surface.Surface,
             col_size: int = WIDTH//SIZE,
             row_size: int = HEIGHT//SIZE) -> None:
        for y in range(self.rows):
            for x in range(self.cols):
                pygame.draw.rect(surface, self.board[y][x][0], pygame.Rect(
                    x*(infoObject.current_w//SIZE), y*(infoObject.current_h//SIZE), infoObject.current_w//SIZE, infoObject.current_h//SIZE))
        pygame.display.flip()

    def set_pixel(self, user: str, x: int, y: int, color: str) -> None:
        print("setting color", user, x, y, color)
        self.board[y][x] = (COLORS[color], user)


class Context:
    def __init__(self, display: Tuple[float, float], board: Tuple[int, int]):
        self.surface: pygame.surface.Surface = pygame.display.set_mode(
            display)
        self.board = Board(*board)
        self.users: Dict[str, str] = {}
        self.timeouts: Dict[str, float] = {}

    __slots__ = "surface", "board", "users", "timeouts", "log"


def load_history(context: Context) -> None:
    # cur = context.db.cursor()
    with open(LOG_FILE, 'r') as f:
        for line in f:
            data = parse_log(line.strip())
            if data is None:
                continue
            timestamp = " ".join(data[:2])

            if data[2] not in ADMINS:
                try:
                    process_serial(data[2:], mktime(strptime(
                        timestamp, '%Y-%m-%d %H:%M:%S')), context)
                except Exception:
                    pass
            else:
                if data[3] != "say":
                    try:
                        process_console(data[2:], mktime(strptime(
                            timestamp, '%Y-%m-%d %H:%M:%S')), context)
                    except Exception:
                        pass


def parse_log(line: str) -> Optional[List[str]]:
    data = re.split(r" +", line)

    if len(data) < 4:
        return None

    return data


def parse(input: str) -> Optional[List[str]]:
    data = re.split(r" +", input)

    if len(data) < 2:
        return None

    return data


def get_user(user_id: str, users: Dict[str, str]) -> str:
    return users[user_id] if user_id in users else "Unknown"


def set_user(user_id: str, user: str, users: Dict[str, str]) -> None:
    users[user_id] = user


def paint(user_id: str,
          args: List[str],
          time: float,
          context: Context) -> None:
    if len(args) != 3:
        print("Invalid number of arguments")
        return

    _x, _y, _color = tuple(args)

    color = _color.lower()

    if not _x.isdecimal() or not _y.isdecimal or color not in COLORS:
        print("Invalid arguments")
        return

    if "." in _x or "." in _y:
        print("decimal")
        return

    x = int(_x)
    y = int(_y)

    if x < 0 or y < 0 or x >= SIZE or y >= SIZE:
        print("Invalid coords")
        return

    if (user_id not in context.timeouts
        or time - context.timeouts[user_id] > PAINT_TIMEOUT
            or user_id in ADMINS):
        context.board.set_pixel(get_user(user_id, context.users), x, y, color)
        context.timeouts[user_id] = time


def user(user_id: str,
         args: List[str],
         time: float,
         context: Context) -> None:
    if len(args) != 1:
        return

    user = args[0]

    set_user(user_id, user, context.users)


def say(user_id: str,
        args: List[str],
        time: float,
        context: Context) -> None:
    if len(args) != 1:
        return
    print("trying to say", args)
    if user_id in ADMINS:
        try:
            f = open(args[0], "r")
            for line in f.readlines():
                data = parse("-1359147492 " + line.lstrip().rstrip())
                if data is None:
                    return
                print("Saying:", data)
                log(data, context)
                process_console(data, time, context)
        except IOError:
            print("Error: File does not appear to exist.")


SERIAL_COMMANDS = {
    "paint": paint,
    "user": user,
}


CONSOLE_COMMANDS = {
    "paint": paint,
    "user": user,
    "say": say
}

matcher = re.compile("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} -?\d+ (paint \d{1,2} \d{1,2} (white|platinum|grey|black|pink|red|orange|brown|yellow|lime|green|cyan|lblue|blue|mauve|purple|WHITE|PLATINUM|GREY|BLACK|PINK|RED|ORANGE|BROWN|YELLOW|LIME|GREEN|CYAN|LBLUE|BLUE|MAUVE|PURPLE)|(user .+)|(say .+))\n")

def log(data: List[str], context: Context) -> None:
    user_id = data[0]
    command = data[1]

    args = data[2:] if len(data) > 2 else []

    out = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    out += " " + str(user_id) + " " + command
    out += " ".join(args) + "\n"

    context.log.write(out)


def process_serial(data: List[str], timestamp: float, context: Context) -> None:
    user_id = data[0]
    command = data[1]

    args = data[2:] if len(data) > 2 else []

    if (command in SERIAL_COMMANDS):
        SERIAL_COMMANDS[command](user_id, args, timestamp, context)


def serial_handler(ser, mask, context: Context) -> None:
    if ser.in_waiting == 0:
        return
    try:
        x = ser.readline().decode("ascii").strip()
    except Exception:
        return
    data = parse(x)
    if data is None:
        return
    print(data)
    log(data, context)
    process_serial(data, time(), context)


def process_console(data: List[str], timestamp: float, context: Context) -> None:
    user_id = data[0]
    command = data[1]

    args = data[2:] if len(data) > 2 else []
    if (command in CONSOLE_COMMANDS):
        CONSOLE_COMMANDS[command](user_id, args, timestamp, context)
    print("Console command: ", data)


def console_handler(console, mask, context: Context) -> None:
    x = console.read().rstrip().lstrip()
    data = parse("-1359147492 " + x)
    if data is None:
        return
    print(data)
    log(data, context)
    process_console(data, time(), context)
    context.board.draw(context.surface)


def draw(context: Context):
    while True:
        context.board.draw(context.surface)
        sleep(1)


if __name__ == '__main__':
    pygame.init()

    infoObject = pygame.display.Info()

    context = Context(
        (infoObject.current_w, infoObject.current_h),
        (SIZE, SIZE))

    load_history(context)

    context.log = open(LOG_FILE, "a")

    drawing = Thread(target=draw, args=tuple([context]))
    drawing.start()

    #with serial.Serial("COM47", 115200) as ser:
    with serial.Serial('/dev/ttyACM0', 115200) as ser:
        m_selector = selectors.DefaultSelector()
        m_selector.register(sys.stdin, selectors.EVENT_READ, console_handler)
        m_selector.register(ser, selectors.EVENT_READ, serial_handler)
        #while True:
        #    sys.stdout.write('>>> ')
        #    sys.stdout.flush()
        #    context.log.flush()

