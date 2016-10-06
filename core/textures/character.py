
class Character:

    def __init__(self, background, chartex, charcolor, overlay, pos): # background, charcolor, overlay : Color/chartex : Sprite/pos : tuple of ints
            self.background = background
            self.character = chartex
            self.charcolor = charcolor
            self.overlay = overlay
            self.pos = pos
