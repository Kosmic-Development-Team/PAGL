from core import game
import core
from core import keyinput
from core.graphics import gui
import Image
from core.graphics import font
from pygame import Color
from flow import signal
import core
import pygame


pressed = False


def press(pt):
    global pressed
    if pt:
        if not pressed:
            print('hello')
            pressed = True
    else:
        if pressed:
            pressed = False



game.timemin = 0.01
game.texturedim = (8, 8)
game.screendim = (60, 40)
game.init()
f = font.Font('C:/Users/Kosmic/Documents/PythonProjects/PRLGL/FONT.png')
ti = Image.open('console.png')

txto = ['                                                            ',
        ' Welcome to PPCM3                                           ',
        '  -Type ls to list files-                                   ',
        ' root@PPCM3:~$                                              ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ',
        '                                                            ']

fc = []
for k in range(40):
    fc.append([])
    for l in range(60):
        fc[k].append(Color(0, 255, 0, 255))

g = gui.Gui((0, 0), 0, [], {}, txto, ti, fc)
g.draw()
pygame.display.update()
game.run()



