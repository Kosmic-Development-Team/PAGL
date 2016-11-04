from pygame import Color
from util.utility import *


class Font:

    def __init__(self, filename):  # filename : string
        try:
            sheet = pygame.image.load(filename).convert()
            self.cw = int(sheet.get_width() / 16.0)
            self.ch = int(sheet.get_height() / 16.0)
            self.chars = []
            for i in range(0, 16):
                for j in range(0, 16):
                    self.chars.append(gettex(sheet, (i * self.cw, j * self.ch, self.cw, self.ch)))
        except pygame.error:
            print('Unable to load sprite sheet ' + filename)

    def drawbasic(self, surface, string, pos):  # surface : Surface/string : string/pos tuple
        count = 0
        for c in string:
            char = self.chars[ord(c)]
            surface.blit(char, char.get_rect().move(pos[0] + self.cw * count, pos[1]))
            count += 1

    def drawback(self, surface, string, backcolors, forecolor, pos):  # surface, string, list of tuples, tuple
        count = 0
        for c in string:
            char = self.chars[ord(c)]
            cr = char.get_rect()
            tile = pygame.Surface((self.cw, self.ch))
            tile.fill(backcolors[count])
            char.set_colorkey(Color(0, 0, 0))
            fore = pygame.Surface((self.cw, self.ch))
            fore.fill(forecolor)
            fore.blit(char, cr)
            fore.set_colorkey(Color(255, 255, 255))
            tile.blit(fore, cr)
            surface.blit(tile, cr.move(pos[0] + self.cw * count, pos[1]))
            count += 1

    def drawfore(self, surface, string, backcolor, forecolors, pos):
        count = 0
        for c in string:
            char = self.chars[ord(c)]
            cr = char.get_rect()
            tile = pygame.Surface((self.cw, self.ch))
            tile.fill(backcolor)
            char.set_colorkey(Color(0, 0, 0))
            fore = pygame.Surface((self.cw, self.ch))
            fore.fill(forecolors[count])
            fore.blit(char, cr)
            fore.set_colorkey(Color(255, 255, 255))
            tile.blit(fore, cr)
            surface.blit(tile, cr.move(pos[0] + self.cw * count, pos[1]))
            count += 1

    def drawfull(self, surface, string, backcolors, forecolors, pos):
        count = 0
        for c in string:
            char = self.chars[ord(c)]
            cr = char.get_rect()
            tile = pygame.Surface((self.cw, self.ch))
            tile.fill(backcolors[count])
            char.set_colorkey(Color(0, 0, 0))
            fore = pygame.Surface((self.cw, self.ch))
            fore.fill(forecolors[count])
            fore.blit(char, cr)
            fore.set_colorkey(Color(255, 255, 255))
            tile.blit(fore, cr)
            surface.blit(tile, cr.move(pos[0] + self.cw * count, pos[1]))
            count += 1
