import pygame
from core.textures.font import Font
from pygame import Color
from pygame import display
import sys
import os


screen = None


def initiate(dim, texdim): #dim and texdim both tuples of ints
    global screen
    screen = display.set_mode((dim[0] * texdim[0], dim[1] * texdim[1]))




def initgame():
    #screen = display.set_mode((500, 300))
    i = 1
    while True:
        screen.fill(pygame.Color(255, 0, 0))
        pygame.draw.rect(screen, Color(255, 255, 255) // Color(12, 34, 6), (225, 125, 50, 50), int(i))
        display.update()
        i *= 1.001
        if i > 600:
            i = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

initiate((64 + 32, 32 + 4), (12, 18))
f = Font('../fonts/AS.png')
f.drawbasic(screen, 'Hello there sirs', (0, 0))
display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
