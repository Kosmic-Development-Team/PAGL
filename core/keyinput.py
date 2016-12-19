from pygame import key
from core import game
from PFRPL.flow import signal
from core import pykeylist

keysigs = {}
takeinput = True


def addallkeys():
    for k in pykeylist.skti:
        keysigs[k] = signal.Signal(False)


def checkkeys():
    if takeinput:
        ka = key.get_pressed()
        for k in list(keysigs.keys()):
            if not keysigs[k].get() == ka[k]:
                keysigs[k].set(ka[k])


def whilekey(k, state):
    return game.update.filtersignal(keysigs[k].filtersignal(signal.Signal(state)))


def whenkey(k, state):
    sh = keysigs[k].filtersignalbool(lambda x: x == state)
    sh.onrun(lambda: print(k))
    return sh


