from core.graphics.guicomponents.component import Component
from core import screen
from core.graphics import font


class Button(Component):
    def __init__(self, pos, dim, text, fontcode, selrun):
        super(self.__class__, self).__init__(pos, dim)
        self.text = text
        self.backcols = None
        self.forecols = None
        self.indents = None
        self.indexfromtext(text)
        self.fontcode = fontcode
        self.selectedrun = selrun

    def keyin(self, key):
        self.selectedrun(key)

    def indexfromtext(self, text):
        self.indents = [[], []]
        for i in range(len(text)):
            txt = text[i]
            t = len(txt)
            self.indents[0].append(t - len(txt.lstrip()))
            self.indents[1].append(self.dim[0] - len(txt.rstrip()))
            text[i] = txt.strip()

    def draw(self):
        f = font.fonts[self.fontcode]
        for i in range(len(self.text)):
            f.drawindent(screen.screen, self.indents[0][i], self.backcols[i],
                         (self.pos[0], self.pos[1] + i))
            if screen.fancy:
                f.drawblend(screen.screen, self.text[i], self.backcols[i][self.indents[0][i]:], self.forecols[i],
                            (self.pos[0] + self.indents[0][i], self.pos[1] + i))
            else:
                f.draw(screen.screen, self.text[i], self.backcols[i][self.indents[0][i]:], self.forecols[i],
                       (self.pos[0] + self.indents[0][i], self.pos[1] + i))
            fo = self.indents[0][i] + len(self.text[i])
            f.drawindent(screen.screen, self.indents[1][i], self.backcols[i][fo:], (self.pos[0] + fo, self.pos[1] + i))

    def selected(self):
        self.selectedrun(None)
