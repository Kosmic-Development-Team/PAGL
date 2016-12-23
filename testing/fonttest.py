from pygame import Color
from pygame import Rect
from pygame import draw
import pygame
from core.graphics.guicomponents import button
from core import screen
from core.graphics import font

screen.fancy = False
screen.initiate((16, 16), (100, 50))
f = font.Font('C:/Users/Kosmic/Documents/PythonProjects/PRLGL/Bisasam_16x16.png')
cb = []
cf = []
draw.rect(screen.screen, Color(128, 64, 32), Rect((0, 0), (500, 500)))
ca = [chr(c) for c in range(200, 231)]
msg = ''
for c in ca:
    msg += str(c)
print(len(msg))
for i in range(len(msg)):
    v = 256.0 / len(msg)
    cb.append(Color(int(i * v), int(i * v), int(i * v), 255))
for i in range(len(msg)):
    v = 128.0 / len(msg)
    cf.append(Color(int(192 - (i * v)), 0, int(192 - (i * v)), 255))
f.draw(screen.screen, msg, cb, cf, (0, 0))
f.drawblend(screen.screen, msg, cb, cf, (0, 1))
f.drawindent(screen.screen, len(msg), cb, (0, 2))
pygame.display.update()

b = button.Button((10, 10), (12, 2), ['  Start',
                                      '       Game'], 0, None)
b.back = [cb, cb]
b.fore = [cf, cf]
b.draw()

pygame.display.update()

while True:
    print(end='')
