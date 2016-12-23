from core import screen
import pygame


fonts = []


def gettex(sheet, rect):
    rect = pygame.Rect(rect)
    image = pygame.Surface(rect.size).convert()
    image.blit(sheet, (0, 0), rect)
    return image


class Font:

    def __init__(self, filename):  # filename : string
        try:
            sheet = pygame.image.load(filename).convert()
            self.cw = int(sheet.get_width() / 16.0)
            self.ch = int(sheet.get_height() / 16.0)
            self.chars = []
            for i in range(0, 16):
                for j in range(0, 16):
                    self.chars.append(gettex(sheet, (j * self.cw, i * self.ch, self.cw, self.ch)))
            self.fontid = len(fonts)
            fonts.append(self)
        except pygame.error:
            print('Unable to load sprite sheet ' + filename)

    def drawindent(self, surface, length, backcols, pos):
        pos = screen.calcraw(pos)
        back = pygame.Surface((self.cw, self.ch))
        rct = back.get_rect()
        for i in range(length):
            back.fill(backcols[i])
            surface.blit(back, rct.move(pos[0] + self.cw * i, pos[1]))

    def getcoltex(self, code, backcol, forecol):
        c = self.chars[code]
        pxs = pygame.PixelArray(c.copy())
        for x in range(self.cw):
            for y in range(self.ch):
                if pxs[x, y] < 8388608:
                    pxs[x, y] = forecol
                else:
                    pxs[x, y] = backcol
        return pxs.make_surface()

    def getblendtex(self, code, backcol, forecol):
        c = self.chars[code]
        pxs = pygame.PixelArray(c.copy())
        for x in range(self.cw):
            for y in range(self.ch):
                pc = pxs[x, y]
                pb = ((pc & 0xff0000) >> 16) / 255.0
                bnd = tuple((pb * backcol[r] + (1 - pb) * forecol[r]) for r in range(3))
                pxs[x, y] = bnd
        return pxs.make_surface()

    def drawbasic(self, surface, string, pos):  # surface : Surface/string : string/pos tuple
        pos = screen.calcraw(pos)
        count = 0
        for c in string:
            char = self.chars[ord(c)]
            surface.blit(char, char.get_rect().move(pos[0] + self.cw * count, pos[1]))
            count += 1

    def draw(self, surface, string, backcols, forecols, pos):
        pos = screen.calcraw(pos)
        chs = [ord(c) for c in string]
        sz = len(chs)
        for i in range(sz):
            c = self.getcoltex(chs[i], backcols[i], forecols[i])
            rct = c.get_rect().move(pos[0] + self.cw * i, pos[1])
            surface.blit(c, rct)

    def drawblend(self, surface, string, backcols, forecols, pos):
        pos = screen.calcraw(pos)
        chs = [ord(c) for c in string]
        sz = len(chs)
        for i in range(sz):
            c = self.getblendtex(chs[i], backcols[i], forecols[i])
            rct = c.get_rect().move(pos[0] + self.cw * i, pos[1])
            surface.blit(c, rct)
