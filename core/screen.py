import pygame

screen = None
dims = None
wh = None
fancy = False


def initiate(dim, texdim):  # dim and texdim both tuples of ints
    global screen
    global dims
    global wh
    dims = dim
    wh = texdim
    screen = pygame.display.set_mode((dim[0] * texdim[0], dim[1] * texdim[1]))


def calcpos(raw):  # takes a tuple position as input and returns a tuple output
    return raw[0] * dims[0], raw[1] * dims[1]
