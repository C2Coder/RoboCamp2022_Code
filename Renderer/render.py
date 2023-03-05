#!/usr/bin/python3

# ============= Libs ============= #

import os
import png
import sys

# ============= Usage ============= #

try:
    size = int(sys.argv[1])
except:
    print(f'Usage ./render.py <size>')
    exit()

# ============= Variables ============= #

out_folder = "out/"
file_name = "render.png"
log_folder = "logs"

color_map = arr = [[(255, 255, 255) for i in range(size)] for j in range(size)]

color_dic = {
    "white": "#FFFFFF",
    "platinum": "#E4E4E4",
    "grey": "#888888",
    "black": "#222222",
    "pink": "#FFA7D1",
    "red": "#E50000",
    "orange": "#E59500",
    "brown": "#A06A42",
    "yellow": "#E5D900",
    "lime": "#94E044",
    "green": "#02BE01",
    "cyan": "#00D3DD",
    "lblue": "#0083C7",
    "blue": "#0000EA",
    "mauve": "#CF6EE4",
    "purple": "#820080"
}

# ============= Funcs ============= #

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# ============= Get data from logs ============= #

for file in os.listdir(f'{log_folder}'):
    f = open(f'{log_folder}/{file}', "r")
    for line in f.readlines():
        cmds = line.split()
        try:
            cmd = cmds[0]
            xp = int(cmds[1])
            yp = int(cmds[2])
            color = cmds[3].lower()
            if cmd != "paint":
                pass
            color_map[yp][xp] = hex_to_rgb(color_dic[color])
        except:
            pass
    f.close()

# ============= Write IMG ============= #

img = []
for y in range(size):
    row = ()
    for x in range(size):
        row = row + color_map[y][x]
    img.append(row)

with open(f'{out_folder}{file_name}', 'wb') as file:
    w = png.Writer(size, size, greyscale=False)
    w.write(file, img)

print(f'Done !!')
