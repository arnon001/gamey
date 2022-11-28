import pygame
import sys


width = 800
height = 600


screen = pygame.display.set_mode((width, height))
path = r"test_icon.jpeg"
width_and_height = (int(width), int(height))
IMAGE = pygame.image.load(path)
# image = pygame.transform.scale(IMAGE, width_and_height)

while True:
    screen.blit(IMAGE, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
