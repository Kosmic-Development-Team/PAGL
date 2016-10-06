import inspect
import pygame


def gettex(sheet, rect):
    rect = pygame.Rect(rect)
    image = pygame.Surface(rect.size).convert()
    image.blit(sheet, (0, 0), rect)
    return image


def islambda(test, args):
    if isinstance(test, type(lambda: 0)) and isinstance(args, int):
        return len(inspect.signature(test).parameters) == args
    return False
