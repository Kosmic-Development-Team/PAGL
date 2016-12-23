from core import screen
from core.graphics import font
from PIL.PngImagePlugin import PngImageFile
from core import guimanager


class Gui:
    # up down right left
    def __init__(self, pos, fontcode, components, compmap, textoverlay, background, foreground):  # background is array of cols or image
        self.pos = pos
        self.dim = (0, 0)
        self.arrownav = True
        self.components = components  # list of components
        for i in range(len(self.components)):
            self.components[i].index = i
        self.map = compmap  # hashmap <int, list <int>>
        self.fontcode = fontcode
        self.current = -1
        self.text = textoverlay
        self.indents = guimanager.indexfromtext(self.text, self.dim)
        self.back = []
        self.fore = []
        self.csize = len(components)

        if isinstance(background, PngImageFile):
            self.back = guimanager.loadimage(background)
        else:
            self.back = background

        self.dim = (len(self.back[0]), len(self.back))

        if isinstance(foreground, PngImageFile):
            self.fore = guimanager.loadimage(foreground)
        else:
            self.fore = foreground

    def clickselect(self, raw):
        click = screen.calcpos(raw)
        comp = None
        for c in self.components:
            if c.contains(click):
                comp = c
                break
        cc = None
        if self.current is not -1:
            cc = self.components[self.current]
        if cc is not comp and cc is not None:
            cc.selected = False
            self.current = -1
        if comp is not None:
            comp.selected = True
            self.current = comp.index

    def keyin(self, key):
        if 273 <= key <= 276 and self.map and self.current is not -1:
            cc = self.current
            self.current = self.map[cc][key - 273]
            if cc is not self.current:
                self.components[cc].selected = False
            if self.current is not -1:
                self.components[self.current].selected = True
        for c in self.components:
            c.keyin(key)

    def draw(self):
        f = font.fonts[self.fontcode]
        if self.back:
            if self.text and self.fore:
                for i in range(len(self.text)):
                    f.drawindent(screen.screen, self.indents[0][i], self.back[i],
                                 (self.pos[0], self.pos[1] + i))
                    if screen.fancy:
                        f.drawblend(screen.screen, self.text[i], self.back[i][self.indents[0][i]:], self.fore[i],
                                    (self.pos[0] + self.indents[0][i], self.pos[1] + i))
                    else:
                        f.draw(screen.screen, self.text[i], self.back[i][self.indents[0][i]:], self.fore[i],
                                 (self.pos[0] + self.indents[0][i], self.pos[1] + i))
                    fo = self.indents[0][i] + len(self.text[i])
                    f.drawindent(screen.screen, self.indents[1][i], self.back[i][fo:],
                                 (self.pos[0] + fo, self.pos[1] + i))
            else:
                for i in range(self.dim[1]):
                    f.drawindent(screen.screen, self.dim[0], self.back[i], (self.pos[0], self.pos[1] + i))
        for gc in self.components:
            gc.draw()

