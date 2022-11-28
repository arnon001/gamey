import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 600))

gui_font = pygame.font.Font("Game Of Squids.ttf", 30)


# default button function
def button_default_function():
    print("button disabled => (enter function when button = Button(button_function=your_button_function))")


class Button:
    def __init__(self, text, width, height, pos, top_rect_color=(255, 255, 255), text_color=(155, 55, 255), button_function=button_default_function):
        # variable
        self.top_rect_color = top_rect_color
        self.button_function = button_function

        # core attributes
        self.pressed = False

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))

        # text
        self.text_surf = gui_font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    # drwing the button on screen
    def draw(self, border_radius=0):
        # drawing the rectabgle
        pygame.draw.rect(screen, self.top_rect_color,
                         self.top_rect, border_radius=border_radius)
        # adding the text
        screen.blit(self.text_surf, self.text_rect)

        # getting the mouse position
        mouse_pos = pygame.mouse.get_pos()
        # checking if mouse is hovering over button and if button is pressed
        if self.top_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.pressed = True
        # exectuting the mouse function when released
        else:
            if self.pressed == True:
                self.button_function()
                self.pressed = False


button = Button("Button", 200, 40, (200, 300))

while True:

    button.draw(50)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
