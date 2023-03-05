#!/usr/bin/python3

# ============= Libs ============= #

import random
import sys

# ============= Usage ============= #

try:
    size = int(sys.argv[1])
    lines = int(sys.argv[2])
except:
    print(f'Usage ./logs_gen.py <size> <lines>')
    exit()

# ============= Variables ============= #

file_num = 0
color_list = ["white",      # 0     #FFFFFF
              "platinum",   # 1     #E4E4E4
              "grey",       # 2     #888888
              "black",      # 3     #222222
              "pink",       # 4     #FFA7D1
              "red",        # 5     #E50000
              "orange",     # 6     #E59500
              "brown",      # 7     #A06A42
              "yellow",     # 8     #E5D900
              "lime",       # 9     #94E044
              "green",      # 10    #02BE01
              "cyan",       # 11    #00D3DD
              "lblue",      # 12    #0083C7
              "blue",       # 13    #0000EA
              "mauve",      # 14    #CF6EE4
              "purple"]     # 15    #820080

# ============= Create Logs ============= #

f = open(f'logs/log{file_num}.txt', "a")

for i in range(lines):
    if f.tell() > 32767:
        print(f'Closing file {file_num}')
        f.close()
        file_num = file_num+1
        f = open(f'logs/log{file_num}.txt', "a")

    f.write(
        f'paint {random.randint(0, size-1)} {random.randint(0, size-1)} {color_list[random.randint(0, len(color_list)-1)]}\n')

f.close

print(f'Done !!')