from PFRPL.flow import signal
from core import screen
from core import keyinput
import pygame
import sys
import nanotime


update = signal.Signal(0.0)
screendim = (100, 50)
texturedim = (16, 16)
closing = signal.Signal(None)
running = False
__quittype = pygame.event.Event(12)
timemin = 0.01


def initiate():
    update.onrun(keyinput.checkkeys)


def run():
    global running
    screen.initiate(screendim, texturedim)
    running = True
    last = int(nanotime.now())
    while running:
        for ev in pygame.event.get():
            if ev == __quittype:
                running = False
        now = last
        dt = 0
        while dt < timemin:
            now = int(nanotime.now())
            dt = (now - last) * 1E-9
        last = now
        update.set(dt)

    closing.run()
    pygame.quit()
    sys.exit(0)
