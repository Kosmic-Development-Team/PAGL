from core import screen


class Gui:
    def __init__(self, pos, dim, components, compmap):
        self.pos = pos
        self.dim = dim
        self.tpos = screen.calcpos(pos)
        self.tdim = screen.calcpos(dim)
        self.components = components
        self.map = compmap
        self.current = 0
        self.csize = len(components)
