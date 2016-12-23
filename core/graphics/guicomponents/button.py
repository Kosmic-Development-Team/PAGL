import core.guimanager
from core.graphics.guicomponents import component
from core import screen
from core.graphics import font


def defaultrun(s, k):
    print('Button:', s.index, s.selected, s.selecagain)


class Button(component.Component):
    def __init__(self, pos, text, fontcode, backcols, forecols, inrun=defaultrun):
        super(self.__class__, self).__init__(pos, (len(backcols[0]), len(backcols)))
        self.text = text
        self.back = backcols
        self.fore = forecols
        self.indents = core.guimanager.indexfromtext(text, self.dim)
        self.fontcode = fontcode
        self.inputrun = inrun  # func-2 whenever key input

    def keyin(self, key):
        self.inputrun(self, key)

    def draw(self):
        f = font.fonts[self.fontcode]
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
            f.drawindent(screen.screen, self.indents[1][i], self.back[i][fo:], (self.pos[0] + fo, self.pos[1] + i))
