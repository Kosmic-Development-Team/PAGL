from core import game
from core.graphics import gui
from core.graphics.guicomponents import button
from core import guimanager
from core.graphics import font
import Image
from pygame import Color
from pygame import display
from core.pykeylist import smti
import pygame
from core import keyinput

#guimanager.onecolor(Color(0, 0, 128, 255), 20, h=2)
ti = (Image.open('b1.png'), Image.open('console.png'))
slc = [guimanager.loadimage(ti[0]), guimanager.onecolor(Color(0, 0, 255, 255), 20, h=2)]


def onup():
    guimanager.draw()
    display.update()


def br(s, k):
    if s.selected:
        if k is pygame.K_RETURN or k in smti:
            print(s.index, 'pressed')
        s.back = slc[1]
    else:
        s.back = slc[0]


def newtxt():
    return ['activation',
            '       button']


game.screendim = (60, 40)
game.texturedim = (8, 8)
game.timemin = 0.01

game.init()
f = font.Font('C:/Users/Kosmic/Documents/PythonProjects/PRLGL/FONT.png')

bts = []
tb = {}
bn = 8
ic = [guimanager.onecolor(Color(255, 255, 255, 255), 20)[0], guimanager.onecolor(Color(128, 128, 128, 255), 20)[0]]

for i in range(bn):
    bts.append(button.Button((1, 1 + 2 * i), newtxt(), 0, slc[0], ic, inrun=br))
    tb[i] = [(i + bn - 1) % bn, (i + bn + 1) % bn, -1, -1]

print(bts)

g = gui.Gui((0, 0), 0, bts, tb, [], ti[1], [])

gn = guimanager.register(g)
guimanager.setsendkey(True, gn)
guimanager.setvisible(True, gn)
game.update.onrun(onup)
game.run()
