from core import screen
from core.graphics import font
from PIL.PngImagePlugin import PngImageFile


class Gui:
    def __init__(self, pos, dim, fontcode, components, compmap, textoverlay, background, foreground):  # background is array of cols or image
        self.pos = pos
        self.dim = dim
        self.slctcomp = 0
        self.arrownav = True
        self.components = components  # hashmap <int, comp>
        self.map = compmap  # hashmap <int, list <int>>
        self.fontcode = fontcode
        self.current = 0
        self.text = textoverlay
        self.back = []
        self.fore = []
        self.csize = len(components)
        if isinstance(background, PngImageFile):
            pxs = background.load()
            for i in range(dim[1]):
                self.back.append([])
                for j in range(dim[0]):
                    self.back[i].append(pxs[j, i])
        else:
            self.back = background
        if isinstance(foreground, PngImageFile):
            pxs = foreground.load()
            for i in range(dim[1]):
                self.fore.append([])
                for j in range(dim[0]):
                    self.fore[i].append(pxs[j, i])
        else:
            self.fore = foreground

    def keyinput(self, key):
        return None

    def draw(self):
        f = font.fonts[self.fontcode]
        if self.back:
            if self.text and self.fore:
                if screen.fancy:
                    for i in range(self.dim[1]):
                        f.drawblend(screen.screen, self.text[i], self.back[i], self.fore[i], (self.pos[0], self.pos[1] + i))
                else:
                    for i in range(self.dim[1]):
                        f.draw(screen.screen, self.text[i], self.back[i], self.fore[i], (self.pos[0], self.pos[1] + i))
            else:
                for i in range(self.dim[1]):
                    f.drawindent(screen.screen, self.dim[0], self.back[i], (self.pos[0], self.pos[1] + i))
        for gc in self.components:
            gc.draw()

