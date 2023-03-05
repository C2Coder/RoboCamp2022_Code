#!/usr/bin/python3

# ========================= Libraries ========================= #

import pygame
import time
import random
import os
import serial
import sys

# ============= Usage ============= #

try:
    port = sys.argv[1]
    baud = int(sys.argv[2])
except:
    print(f'Usage ./snak.py <port> <baud>')
    print(f'Example: ./snak.py /dev/ttyACM0 115200')
    exit()

# ========================= Variables ========================= #

speed_of_snake = 4

GAME_SIZE = 750

game_squares = 15

pixel_size = GAME_SIZE / game_squares

background_color = pygame.Color(200, 200, 200)
right_side_color = pygame.Color(60, 60, 60)
text_color = pygame.Color(220, 220, 220)
snake_color = pygame.Color(50, 50, 50)
behind_head_color = pygame.Color(40, 40, 40)
head_color = pygame.Color(30, 30, 30)
food_color = pygame.Color(235, 66, 23)

display_screen = pygame.display.set_mode((GAME_SIZE + 250, GAME_SIZE))

game_clock = pygame.time.Clock()

head_pos = [5*pixel_size, 3*pixel_size]

snake_body = [
    [5*pixel_size, 3*pixel_size],
    [4*pixel_size, 3*pixel_size],
    [3*pixel_size, 3*pixel_size],
    [2*pixel_size, 3*pixel_size]
]

food_pos = [
    random.randint(1, (GAME_SIZE//pixel_size)) * pixel_size,
    random.randint(1, (GAME_SIZE//pixel_size)) * pixel_size
]
generate_fruit = True
game_running = True

wanted_direction = 'right'
snake_direction = 'right'

directions = {
    "up": -90,
    "down": 90,
    "left": 0,
    "right": 180
}

player_score = 0
restart_game = False

# ========================= Functions ========================= #

def set_variables():
    global head_pos, snake_color, snake_body, food_pos, generate_fruit, wanted_direction, snake_direction, pixel_size, GAME_SIZE, player_score, restart_game, game_running
    head_pos = [5*pixel_size, 3*pixel_size]

    snake_body = [
    [5*pixel_size, 3*pixel_size],
    [4*pixel_size, 3*pixel_size],
    [3*pixel_size, 3*pixel_size],
    [2*pixel_size, 3*pixel_size]
    ]

    food_pos = [
        random.randint(1, (GAME_SIZE//pixel_size)) * pixel_size,
        random.randint(1, (GAME_SIZE//pixel_size)) * pixel_size
    ]
    game_running = True
    generate_fruit = True
    
    wanted_direction = 'right'
    snake_direction = 'right'
    player_score = 0
    restart_game = False

def display_right_panel():
    global display_screen, player_score, head_pos, scaled_arrow, snake_direction
    labelFont = pygame.font.Font('font.ttf', 45)
    scoreFont = pygame.font.Font('font.ttf', 40)
    highScoreFont = pygame.font.Font('font.ttf', 40) 
    positionFont = pygame.font.Font('font.ttf', 40)

    scoreLabel = labelFont.render('Score', True, text_color)
    score = scoreFont.render(str(player_score), True, text_color)
    highScoreLabel = labelFont.render('Highscore', True, text_color)
    highScore = highScoreFont.render(str(high_score), True, text_color)
    positionLabel = labelFont.render('Position', True, text_color)
    x_position = positionFont.render(
        f'X: {int(head_pos[0]/pixel_size)}', True, text_color)
    y_position = positionFont.render(
        f'Y: {int(head_pos[1]/pixel_size)}', True, text_color)

    scoreLabelRect = scoreLabel.get_rect()
    scoreRect = score.get_rect()
    highScoreLabelRect = highScoreLabel.get_rect()
    highScoreRect = highScore.get_rect()
    positionLabelRect = positionLabel.get_rect()
    x_positionRect = x_position.get_rect()
    y_positionRect = y_position.get_rect()

    scoreLabelRect.center = (GAME_SIZE + 125, 50)
    scoreRect.center = (GAME_SIZE + 125, 100)
    highScoreLabelRect.center = (GAME_SIZE + 125, 175)
    highScoreRect.center = (GAME_SIZE + 125, 225)
    positionLabelRect.center = (GAME_SIZE + 125, 300)
    x_positionRect.center = (GAME_SIZE + 125, 350)
    y_positionRect.center = (GAME_SIZE + 125, 400)

    display_screen.blit(scoreLabel, scoreLabelRect)
    display_screen.blit(score, scoreRect)
    display_screen.blit(highScoreLabel, highScoreLabelRect)
    display_screen.blit(highScore, highScoreRect)
    display_screen.blit(positionLabel, positionLabelRect)
    display_screen.blit(x_position, x_positionRect)
    display_screen.blit(y_position, y_positionRect)

    rotated_arrow = pygame.transform.rotate(
        scaled_arrow, directions[snake_direction.lower()])
    display_screen.blit(rotated_arrow, (GAME_SIZE + 75, 475))

def write_highscore():
    global player_score
    f = open("highscore.txt", "w")
    f.write(str(player_score))
    f.close()

def run_game():
    global game_running, wanted_direction, snake_direction, player_score, snake_body, head_pos, food_pos, food_color, generate_fruit, ser
    while game_running:
        try:
            cmd = str(ser.readline()).lstrip("b'").rstrip("'\\r\\n")
            cmd = cmd.replace("'", "")
            cmds = cmd.split()
            if cmds != []:
                print(f'{cmds[0]} >>> {cmds[1]}')
                if cmds[1] == "up":
                    wanted_direction = "up"
                elif cmds[1] == "down":
                    wanted_direction = "down"
                elif cmds[1] == "left":
                    wanted_direction = "left"
                elif cmds[1] == "right":
                    wanted_direction = "right"
        except:
            continue

        # keyboard handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_UP:
                    wanted_direction = 'up'
                elif event.key == pygame.K_DOWN:
                    wanted_direction = 'down'
                elif event.key == pygame.K_LEFT:
                    wanted_direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    wanted_direction = 'right'

        # pygame screen clear
        display_screen.fill(right_side_color)
        pygame.draw.rect(display_screen, background_color,
                         pygame.Rect(0, 0, GAME_SIZE, GAME_SIZE))

        # check wanted direction
        if wanted_direction == 'up' and snake_direction != 'down':
            snake_direction = 'up'
        elif wanted_direction == 'down' and snake_direction != 'up':
            snake_direction = 'down'
        elif wanted_direction == 'left' and snake_direction != 'right':
            snake_direction = 'left'
        elif wanted_direction == 'right' and snake_direction != 'left':
            snake_direction = 'right'

        # move snake
        last_head_pos = head_pos

        if snake_direction == 'up':
            head_pos[1] -= pixel_size
        elif snake_direction == 'down':
            head_pos[1] += pixel_size
        elif snake_direction == 'left':
            head_pos[0] -= pixel_size
        elif snake_direction == 'right':
            head_pos[0] += pixel_size

        # snake colisions
        if head_pos[0] < 0 or head_pos[0] > GAME_SIZE - pixel_size:
            head_pos = last_head_pos
            game_running = False
        elif head_pos[1] < 0 or head_pos[1] > GAME_SIZE - pixel_size:
            head_pos = last_head_pos
            game_running = False

        for block in snake_body[1:]:
            if head_pos[0] == block[0] and head_pos[1] == block[1]:
                head_pos = last_head_pos
                game_running = False

        if (game_running):
            # check if snake eats food
            if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
                player_score += 1
                generate_fruit = True
            else:
                snake_body.pop()

            # create new body part at head_pos
            snake_body.insert(0, list(head_pos))

        # generate food (weird way, but it works)
        if generate_fruit:
            x_tmp_pos = random.randint(
                1, (GAME_SIZE//pixel_size)-1) * pixel_size
            y_tmp_pos = random.randint(
                1, (GAME_SIZE//pixel_size)-1) * pixel_size
            if [x_tmp_pos, y_tmp_pos] in snake_body:
                x_tmp_pos = random.randint(
                    1, (GAME_SIZE//pixel_size)-1) * pixel_size
                y_tmp_pos = random.randint(
                    1, (GAME_SIZE//pixel_size)-1) * pixel_size
                if [x_tmp_pos, y_tmp_pos] in snake_body:
                    x_tmp_pos = random.randint(
                        1, (GAME_SIZE//pixel_size)-1) * pixel_size  # give up
                    y_tmp_pos = random.randint(
                        1, (GAME_SIZE//pixel_size)-1) * pixel_size
            x_pos = x_tmp_pos
            y_pos = y_tmp_pos

            food_pos = [
                x_pos, y_pos
            ]
        generate_fruit = False

        # draw snake
        for position in snake_body:
            pygame.draw.rect(display_screen, snake_color, pygame.Rect(
                position[0], position[1], pixel_size, pixel_size))

        pygame.draw.rect(display_screen, head_color, pygame.Rect(
            snake_body[0][0], snake_body[0][1], pixel_size, pixel_size))
        pygame.draw.rect(display_screen, behind_head_color, pygame.Rect(
            snake_body[1][0], snake_body[1][1], pixel_size, pixel_size))

        pygame.draw.rect(display_screen, food_color, pygame.Rect(
            food_pos[0], food_pos[1], pixel_size, pixel_size))

        # draw score
        display_right_panel()

        # update and framerate stuff
        pygame.display.update()
        game_clock.tick(speed_of_snake)

# ========================= Main Loop ========================= #

pygame.display.set_caption('SNAK')
pygame.init()


# arrow img
arrow = pygame.image.load("arrow.png")
scaled_arrow = pygame.transform.scale(arrow, (100, 100))


# create highscore file if needed
if not os.path.isfile("highscore.txt"):
    f = open("highscore.txt", "w")
    f.write("10")
    f.close()


# read highscore
f = open("highscore.txt", "r")
high_score = int(f.readline().rstrip().lstrip())
f.close()

ser = serial.Serial(port, baud, timeout=0.1)

while True:
    set_variables()

    run_game()

    #print("Game Over")
    if player_score > high_score:
        high_score = player_score
        write_highscore()

    while not restart_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_RETURN:
                    restart_game = True
        try:
            cmd = str(ser.readline()).lstrip("b'").rstrip("'\\r\\n")
            cmd = cmd.replace("'", "")
            cmds = cmd.split()
            if cmds != []:
                print(f'{cmds[0]} >>> {cmds[1]}')
                if cmds[1] == "restart":
                    restart_game = True
        except:
            continue


        pygame.display.update()
        game_clock.tick(10)
    
    #print("game restarted")
    restart_game = False
