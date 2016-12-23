from core import screen


class Component:
    def __init__(self, pos, dim):
        self.pos = pos
        self.dim = dim
        self.tpos = screen.calcraw(pos)
        self.tdim = screen.calcraw(dim)
        self.selected = False
        self.index = -1

    def contains(self, pos):
        print(pos)
        return (self.pos[0] <= pos[0] < self.pos[0] + self.dim[0])\
            and (self.pos[1] <= pos[1] < self.pos[1] + self.dim[1])

    def draw(self):
        return None

    def keyin(self, key):
        return None
