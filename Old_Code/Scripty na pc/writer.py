import pyautogui
import time

f = open("in.txt")

for line in f.readlines():
    pyautogui.write(line)
    time.sleep(0.05)
    pyautogui.press('enter')
    time.sleep(0.05)