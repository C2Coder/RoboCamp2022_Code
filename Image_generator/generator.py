#!/usr/bin/python3

# ============= Libs ============= #

import images
import os
import numpy

# ============= Variables ============= #


img = images.rickroll

y_size = len(img)
x_size = len(img[0])

upscale_rate = 4

upscale = numpy.zeros(x_size*y_size*upscale_rate*upscale_rate, dtype=int).reshape(x_size*upscale_rate, y_size*upscale_rate).tolist()

color_list = ["white",
              "platinum",
              "grey",
              "black",
              "pink",
              "red",
              "orange",
              "brown",
              "yellow",
              "lime",
              "green",
              "cyan",
              "lblue",
              "blue",
              "mauve",
              "purple"]

cmd_list = []

x_offset = 0
y_offset = 0

# ============= Generate commands ============= #

print(f'X: {x_size}, Y: {y_size}')
print(img)
print(upscale)

try:
    os.remove("data.txt")
except:
    pass

f = open("data.txt", "a")

for y in range(y_size*upscale_rate):
    for x in range(x_size*upscale_rate):
        print(f'X: {x} Y: {y} Xd: {int(x/upscale_rate)} Yd: {int(y/upscale_rate)}')
        upscale[x][y] = img[int(y/upscale_rate)][int(x/upscale_rate)]
        f.write(f'paint {x + x_offset} {y + y_offset} {color_list[upscale[x][y]]}\n')

f.close()

print(f'Done !!')