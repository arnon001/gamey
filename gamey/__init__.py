# importing the base library
import pygame as goomy
from gamey import PKey
import sys
import keyboard

# activating the base library
goomy.init()

# public variables
clock = goomy.time.Clock()
_default_gamey_font = "gamey/gamey_default.otf"
default_gamey_font = goomy.font.Font(_default_gamey_font, 30)
gamey_user_text_input = ""


# global varibales
screen_width = 0
screen_height = 0


# killing the program
def quit_prog():
    goomy.quit()
    sys.exit()


# Printing a red colored error to console
def create_error(error):
    print(f"\033[1;31;40m [ERROR]: {error}")
    quit_prog()


# Main pygame loop
def main_loop():
    global gamey_user_text_input
    # when an event is happening
    for event in goomy.event.get():
        # check if event is quit
        if event.type == goomy.QUIT:
            # quiting the program
            quit_prog()

    # updating the screen every time the loop is done
    goomy.display.flip()
    clock.tick(60)


# Default thing for button to do if not provided
def button_default_function():
    create_error(
        "button disabled => (enter function when button = Button(button_function=your_button_function))")


# Screen Class
class Screen:
    screen = goomy.display.set_mode((1, 1))

    # Constructor - when creating a screen this will be run
    def __init__(self, screen=0, width=200, height=200, title="gamey new window", icon='img\gamey_logo.png'):
        global screen_height, screen_width
        # local screen variables
        self.width = width
        self.height = height
        self.title = title
        self.icon = icon
        self.screen = screen

        screen_width, screen_height = self.width, self.height

        # creating the screen
        self.screen = goomy.display.set_mode(
            (self.width, self.height))

        # screen caption - title
        goomy.display.set_caption(self.title)

        # loading the icon
        programIcon = goomy.image.load(self.icon)
        # putting it in the window
        goomy.display.set_icon(programIcon)

    # Change background function
    def bg_color(self, r, g, b):
        # actually doing it
        self.screen.fill((r, g, b))


# Text
class Text(Screen):
    # Constructor
    def __init__(self, x=0, y=0, w=100, h=100, color=(255, 255, 255), bg_color=(0, 0, 155), font=_default_gamey_font, font_size=12, text="Text"):
        # defining the public variables of the text
        self.font = font
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = color
        self.text_bg_color = bg_color
        self.font_size = font_size
        self.text = text

        # variable that define the text
        font = goomy.font.Font(font, font_size)
        self.text_surf = font.render(
            self.text, True, self.color, self.text_bg_color)
        self.text_rect = self.text_surf.get_rect()

        self.text_rect.center = (x, y)

    # drawing the text on screen
    def draw(self):
        Screen.screen.blit(self.text_surf, self.text_rect)

    def move(self, x: float, y: float) -> None:
        self.text_rect.move(x, y)


# Button class
class Button(Screen):
    # Constructor
    def __init__(self, text="Button", width=200, height=100, x=0, y=0, top_rect_color=(255, 255, 255), text_color=(155, 55, 255), command=button_default_function):
        # variable
        self.top_rect_color = top_rect_color
        self.button_function = command

        # core attributes
        self.pressed = False

        # top rectangle
        self.top_rect = goomy.Rect((x, y), (width, height))

        # text
        self.text_surf = default_gamey_font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    # drwing the button on screen
    def draw(self, border_radius=0):
        # drawing the rectabgle
        goomy.draw.rect(Screen.screen, self.top_rect_color,
                        self.top_rect, border_radius=border_radius)
        # adding the text
        Screen.screen.blit(self.text_surf, self.text_rect)

        # getting the mouse position
        mouse_pos = goomy.mouse.get_pos()
        # checking if mouse is hovering over button and if button is pressed
        if self.top_rect.collidepoint(mouse_pos) and goomy.mouse.get_pressed()[0]:
            self.pressed = True
        # exectuting the mouse function when released
        else:
            if self.pressed == True:
                self.button_function()
                self.pressed = False


# Image class
class Image(Screen):
    # Global variables
    global screen_height, screen_width

    # Constructor
    def __init__(self, path='./img/gamey_logo.png', x=0, y=0, width=None, height=None):
        # variables
        self.x = x
        self.y = y
        self.path = path
        self.width = width
        self.height = height

        if path != "" and self.width != None and self.height != None:
            # loading the image
            width_and_height = (int(self.width), int(self.height))
            IMAGE = goomy.image.load(self.path)
            self.image = goomy.transform.scale(IMAGE, width_and_height)
        elif path != "":
            self.image = goomy.image.load(self.path)
        else:
            create_error("Image path is not correct/not existing")

    # Loading the image to the screen
    def load(self):
        Screen.screen.blit(self.image, (self.x, self.y))


# Functions class
"""
! NOT WORKING !
! FIX !
class movement(Screen):

    def move_by_key_press(self, item, pixels: float, key_list):
        if len(key_list) > 4 and len(key_list) < 9:
            if keyboard.is_pressed(key_list[0]) or keyboard.is_pressed(key_list[4]):
                self.move_up(item, pixels)
            
            elif keyboard.is_pressed(key_list[1]) or keyboard.is_pressed(key_list[5]):
                self.move_left(item, pixels)
            
            elif keyboard.is_pressed(key_list[2]) or keyboard.is_pressed(key_list[6]):
                self.move_down(item, pixels)
            
            elif keyboard.is_pressed(key_list[3]) or keyboard.is_pressed(key_list[7]):
                self.move_right(item, pixels)
        else:
            if keyboard.is_pressed(key_list[0]):
                self.move_up(item, pixels)
            
            elif keyboard.is_pressed(key_list[1]):
                self.move_left(item, pixels)
            
            elif keyboard.is_pressed(key_list[2]):
                self.move_down(item, pixels)
            
            elif keyboard.is_pressed(key_list[3]):
                self.move_right(item, pixels)



    def move_up(item, pixels: float):
        item.y -= pixels

    def move_down(item, pixels: float):
        item.y += pixels

    def move_left(item, pixels: float):
        item.x -= pixels

    def move_right(item, pixels: float):
        item.x += pixels

"""