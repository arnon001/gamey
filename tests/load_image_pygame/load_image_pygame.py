import pygame
import sys


width = 800
height = 600


screen = pygame.display.set_mode((width, height))

image = pygame.image.load('tests/load_image_pygame/gamey_logo.png')

while True:

    screen.blit(image, (width/2, height/2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
