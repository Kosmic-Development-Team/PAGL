from pygame import key
from PFRPL.flow import signal

keysigs = {}
takeinput = True


def addkeycheck(k):
    keysigs[k] = (signal.Signal(False))


def checkkeys():
    if takeinput:
        ka = key.get_pressed()
        for k in list(keysigs.keys()):
            keysigs[k].set(ka[k])

