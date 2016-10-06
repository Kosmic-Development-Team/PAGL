from pygame import draw
from pygame import Color
from util.utility import *


class Font:

    def __init__(self, filename): #filename : string
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

    def drawbasic(self, surface, string, pos): # surface : Surface/string : string/pos tuple
        count = 0
        for c in string:
            char = self.chars[ord(c)]
            surface.blit(char, char.get_rect().move(pos[0] + self.cw * count, pos[1]))
            count += 1
