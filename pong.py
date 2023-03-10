# import keyboard
from gamey import *
from gamey import funcs
import random

screen = Screen(width=800,height=600)

player_1_y, player_2_y= 225,225

ball_x, ball_y = 400,300
ball_direction, ball_speed = random.choice([-2,2]), random.choice([-2,2])

while True:
    screen.bg_color(0,0,0)

    # ! Draw seperator line ! #
    seperator_y = 0
    while seperator_y < 800:
        Draw.rect(x=395, w=10, y=seperator_y, h=25, color=(150,150,150))
        seperator_y += 50



    # ! Object Creation ! #
    player_1 = Draw.rect(x=25, y=player_1_y, w=25, h=150)
    player_2 = Draw.rect(x=750, y=player_2_y, w=25, h=150)
    ball = Draw.circle(x=ball_x,y=ball_y, radius=10)

    # ! Movement ! #
    # Player 1 movement #
    if keyboard.is_pressed("s"):
        player_1_y += 6
    elif keyboard.is_pressed("w"):
        player_1_y -= 6

    # Player 2 movement #
    if keyboard.is_pressed("down"):
        player_2_y += 6
    elif keyboard.is_pressed("up"):
        player_2_y -= 6

    # ball movement #
    ball_x += ball_speed
    ball_y += ball_direction

    # ! Collide Handler ! #
    # player wall collision #
    if player_1_y < 0:
        player_1_y = 0
    elif player_1_y > 450:
        player_1_y = 450
    
    if player_2_y < 0:
        player_2_y = 0
    elif player_2_y > 450:
        player_2_y = 450
    
    # ball collision #
    if ball_y > 590 or ball_y < 10:
        ball_direction *= -1
    elif ball_x > 740 and ball_y > player_2_y and ball_y < player_2_y+150 or ball_x < 60  and ball_y > player_1_y and ball_y < player_1_y+150:
        ball_direction = random.choice([-4,4,-2,-3,2,3])
        ball_speed *=-1
    elif ball_x > 790 or ball_x < 10:
        quit_prog()    


    # ! main loop ! #
    main_loop()