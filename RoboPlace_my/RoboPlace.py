

# ========================= LIBRARIES ========================= #

import serial
import pygame

# ========================= PYGAME INIT ========================= #

pygame.init()

clock = pygame.time.Clock()

# ========================= WINDOWS STUFF ========================= #

diplay_size = 800
pixels = 100

pixel_size = diplay_size / pixels

# ========================= VARIALBES ========================= #

interval = 2000
lastTicks = 0

ID_cooldown = 10000   # 10 seconds
ID_timeouts = []
ID_timers = []
changes = []

# ========================= COLORS ========================= #

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

COLOR = {
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

# ========================= WINDOWS STUFF ========================= #

# Set up the drawing window
diplay = pygame.display.set_mode([diplay_size, diplay_size])

pygame.display.set_caption('RoboPlace')

# ========================= DRAWING STUFF ========================= #

# Fill the background with white
diplay.fill(COLOR["white"])


def draw_pixel(x, y, color):
    pygame.draw.rect(
        diplay, COLOR[color], (x * pixel_size, y * pixel_size, pixel_size, pixel_size))


def draw_changes():
    global changes
    for change in changes:
        try:
            draw_pixel(int(change[0]), int(change[1]), change[2])
        except:
            pass
    changes = []

# ========================= TIMEOUTS HANDLER ========================= #

def timeouts_handler():
    global ID_timeouts
    global ID_timers

    cur_time = pygame.time.get_ticks()
    for timer in ID_timers:
        if timer + ID_cooldown < cur_time:
            ID_index = ID_timers.index(timer) # get index of ID in list
            ID_timeouts.pop(ID_index)
            ID_timers.pop(ID_index)
            #print(ID_timers)
            #print(ID_timeouts)
        else:
            continue

# ========================= SERIAL SETUP ========================= #

ser = serial.Serial('COM47', 115200, timeout=0.1)

# ========================= MAIN LOOP ========================= #

running = True
while running:
    if pygame.time.get_ticks() - lastTicks > interval:
        lastTicks = lastTicks + interval
        draw_changes()
        timeouts_handler()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    msg = ser.read(ser.in_waiting)
    msg = msg.decode('utf-8')
    if len(msg) > 12:
        msg = msg.strip()
        cmds = msg.split(" ")
        
        if cmds[1] != "paint":
            #print(f'Not paint command ({cmds[1]})')
            continue

        serialID = cmds[0]
        if serialID in ID_timeouts:
            #print(f'ID is in timeouts (id:{cmds[0]})')
            continue
        ID_timeouts.append(serialID)
        ID_timers.append(pygame.time.get_ticks())
        try:
            cmds[4] = str(cmds[4]).lower()
            print(f'{cmds[0]} >>> {cmds[1]} {cmds[2]} {cmds[3]} {cmds[4]}')
            changes.append([cmds[2], cmds[3], cmds[4]])
        except:
            #print("Error while reading (Line 137)")
            continue
        #print(ID_timeouts)
        #print(changes)

    clock.tick(10)



pygame.quit()
