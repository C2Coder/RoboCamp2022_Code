#!/usr/bin/python3

# ============= Libs ============= #

import pyautogui
import time
import sys
import pyperclip

# ============= Variables ============= #

delay = 1000     # between lines (ms)

# ============= File ============= #

try:
    f = open("data.txt", "r")
except:
    print("data.txt does not exist !!!")
    sys.exit()

# ============= Timer ============= #

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

# ============= Write on Keaboard ============= #

print("\nStarted")


for line in f.readlines():
    pyperclip.copy(line)
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy('')
    time.sleep(delay/1000)
