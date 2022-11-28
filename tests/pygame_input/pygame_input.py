import pygame
import input_functions

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 800
Y = 600


screen = pygame.display.set_mode((X, Y))

text = input_functions.listen()

font = pygame.font.Font('Game Of Squids.ttf', 22)
text = font.render(text, True, green, None)
textRect = text.get_rect()
while True:

    rect2 = pygame.Rect(0, 0, textRect.width, textRect.height+5)
    pygame.draw.rect(screen, (200, 100, 180), rect2, 2)

    screen.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
