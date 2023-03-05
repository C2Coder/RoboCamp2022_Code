#!/usr/bin/python3

# ============= Libs ============= #

import os
import png
import numpy as np
import sys

# ============= Usage ============= #

try:
    size = int(sys.argv[1])
except:
    print(f'Usage ./heatmap.py <size>')
    exit()

# ============= Variables ============= #

out_folder = "out/"
file_name = "heatmap.png"
log_folder = "logs"

data = np.zeros((size*size,), dtype=int).reshape(size, size).tolist()
clrs = np.zeros((size*size,), dtype=int).reshape(size, size).tolist()

# ============= Funcs ============= #

def scale(value, minFrom, maxFrom, minTo, maxTo):
    mappedValue = minTo + (maxTo - minTo) * ((value - minFrom) / (maxFrom - minFrom))
    return int(mappedValue)

# ============= Get data from logs ============= #

for file in os.listdir(f'{log_folder}'):
    f = open(f'{log_folder}/{file}', "r")
    for line in f.readlines():
        cmds = line.split()
        try:
            cmd = cmds[0]
            xp = int(cmds[1])
            yp = int(cmds[2])
            color = cmds[3]
            if cmd != "paint":
                pass
            data[xp][yp] = data[xp][yp] + 1
        except:
            pass
    f.close()
print(data)


# ============= Data to Color  ============= #


m_val = np.amax(data)
#m_val = 8
for y in range(size):
    for x in range(size):
        clrs[x][y] = scale(data[x][y], 0, m_val, 0, 255)

# ============= Write IMG ============= #

img = []
for y in range(size):
    row = ()
    for x in range(size):
        row = row + (clrs[y][x], clrs[y][x], clrs[y][x])
    img.append(row)

with open(f'{out_folder}{file_name}', 'wb') as file:
    w = png.Writer(size, size, greyscale=False)
    w.write(file, img)

print(f'Done !!')