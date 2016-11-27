from core import game
from core import keyinput
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
game.initiate()
game.screendim = (25, 25)
keyinput.addkeycheck(pygame.K_h)
keyinput.keysigs[pygame.K_h].filtersignalbool(lambda x: x).onrun(lambda: press(True))
keyinput.keysigs[pygame.K_h].filtersignalbool(lambda x: not x).onrun(lambda: press(False))
game.run()



