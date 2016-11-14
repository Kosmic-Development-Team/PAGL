from core import screen
import abc


class Component:
    def __init__(self, pos, dim):
        self.pos = pos
        self.dim = dim
        self.tpos = screen.calcpos(pos)
        self.tdim = screen.calcpos(dim)

    def draw(self):
        return None

    def selected(self):
        return None

    def keyin(self, key):
        return None
