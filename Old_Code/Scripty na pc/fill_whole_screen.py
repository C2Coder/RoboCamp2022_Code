import time
import keyboard
import sys

colors = ['WHITE',
        'PLATINUM',
        'GREY',
        'BLACK',
        'PINK',
        'RED',
        'ORANGE',
        'BROWN',
        'YELLOW',
        'LIME',
        'GREEN',
        'CYAN',
        'LBLUE',
        'BLUE',
        'MAUVE',
        'PURPLE']

while(True):
    color = input("Input Color \nList of colors: WHITE, PLATINUM, GREY, BLACK, PINK, RED, ORANGE, BROWN, YELLOW, LIME, GREEN, CYAN, LBLUE, BLUE, MAUVE, PURPLE \n -> ")
    if  color in colors:
        for t in reversed(range(0,6)):
            print(t)
            if t == 0:
                print("Starting!")
            else:
                time.sleep(1)
        for x in range(0, 100):
            for y in range(0, 100):
                message = "paint " + str(x) + " " + str(y) + " " + color  + "\n"
                keyboard.write(message)
                time.sleep(0.07)
    else:
        sys.exit("Colors is not valid")


