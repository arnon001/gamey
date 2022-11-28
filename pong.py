# import keyboard
from gamey import *
import gamey

screen = Screen(width=800,height=600)

x = 300
y = 300

while True:
    screen.bg_color(255,255,255)

    rect_1 = Text(x=x, y=y, text="Hello darkness")
    
    if keyboard.is_pressed("d"):
        x += 2
    if keyboard.is_pressed("a"):
        x -= 2

    if keyboard.is_pressed("s"):
        y += 2
    if keyboard.is_pressed("w"):
        y -= 2


    
    rect_1.draw()
    rect_1.move(x, y)

    main_loop()