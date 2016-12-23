from core.pykeylist import skti
from core.pykeylist import smti
from core import keyinput
import pygame


registered = {}
sendinput = []
visible = []
curid = -1


def init():
    for k in skti:
        keyinput.whenkey(k, True).onkeyrun(lambda x: keyin(x))
    for m in smti:
        keyinput.whenmouse(m, True).onkeyrun(lambda x: keyin(x))


def register(g):
    global curid
    curid += 1
    registered[curid] = g
    return curid


def keyin(key):
    clk = key in smti
    for g in sendinput:
        rg = registered[g]
        if clk:
            rg.clickselect(pygame.mouse.get_pos())
        rg.keyin(key)


def setsendkey(snd, guiid):
    if guiid in registered.keys():
        cg = guiid in sendinput
        if snd and not cg:
            sendinput.append(guiid)
        elif not snd and cg:
            sendinput.remove(guiid)


def setvisible(vis, guiid):
    if guiid in registered.keys():
        cg = guiid in visible
        if vis and not cg:
            visible.append(guiid)
        elif not vis and cg:
            visible.remove(guiid)


def onecolor(col, w, h=1):
    ca = []
    for i in range(h):
        ca.append([])
        for j in range(w):
            ca[i].append(col)
    return ca


def loadimage(img):
    ica = []
    pxs = img.load()
    w, h = img.size
    for i in range(h):
        ica.append([])
        for j in range(w):
            ica[i].append(pxs[j, i])
    return ica


def draw():
    for g in visible:
        cdg = registered[g]
        cdg.draw()


def indexfromtext(text, dim):
    indents = [[], []]
    for i in range(len(text)):
        txt = text[i]
        t = len(txt)
        indents[0].append(t - len(txt.lstrip()))
        indents[1].append(dim[0] - len(txt.rstrip()))
        text[i] = txt.strip()
    return indents