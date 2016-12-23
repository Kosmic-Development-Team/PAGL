import pygame
from core import game
from PFRPL.flow import signal
from core import pykeylist
import math

keysigs = {}
mousesigs = {}
deltamouse = signal.Signal(0.0)
prevpos = (0, 0)
takeinput = True


def init():
    for k in pykeylist.skti:
        keysigs[k] = Keysig(k)
    for m in range(3):
        mousesigs[m] = Keysig(m)


def checkkeys():
    global prevpos
    if takeinput:
        ka = pygame.key.get_pressed()
        ma = pygame.mouse.get_pressed()
        curpos = pygame.mouse.get_pos()
        deltamouse.set(math.sqrt((prevpos[0] - curpos[0]) ** 2 + (prevpos[1] - curpos[1]) ** 2))
        prevpos = curpos
        for k in list(keysigs.keys()):
            if not keysigs[k].get() == ka[k]:
                keysigs[k].set(ka[k])
        for m in list(mousesigs.keys()):
            if not mousesigs[m].get() == ma[m]:
                mousesigs[m].set(ma[m])


def whilekey(k, state):
    return Keysig(k, sig=game.update.filtersignal(keysigs[k].filtersignal(signal.Signal(state))))


def whenkey(k, state):
    return Keysig(k, sig=keysigs[k].filtersignalbool(lambda x: x == state))


def whilemouse(k, state):
    return Keysig(k, sig=game.update.filtersignal(mousesigs[k].filtersignal(signal.Signal(state))))


def whenmouse(k, state):
    return Keysig(k, sig=mousesigs[k].filtersignalbool(lambda x: x == state))


class Keysig(signal.Signal):
    def __init__(self, k, sig=None):
        super(Keysig, self).__init__(False)
        self.key = k
        if sig is not None:
            self._parents = sig._parents
            self._children = sig._children
            self._tocall = sig._tocall
            self._value = sig._value

    def onkeyrun(self, operator):
        def op():
            operator(self.key)
        self.onrun(op)
