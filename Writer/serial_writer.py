#!/usr/bin/python3

# ============= Libs ============= #

import time
import sys

import serial

# ============= Usage ============= #

try:
    port = sys.argv[1]
    baud = int(sys.argv[2])
    delay = int(sys.argv[3])
except:
    print(f'Usage ./serial_writer.py <port> <baud> <delay>')
    exit()

# ========================= SERIAL SETUP ========================= #

ser = serial.Serial(port, baud)

# ============= Write on Keaboard ============= #

print("\nStarted")

f = open("data.txt", "r")

for line in f.readlines():
    line = line.rstrip("\n")
    ser.write(bytes(line, 'utf-8'))
    time.sleep(delay/1000)
