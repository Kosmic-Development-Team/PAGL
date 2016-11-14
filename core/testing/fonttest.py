from pygame import Color
from pygame import Rect
from pygame import draw
from core.graphics.guicomponents import button
from core import screen
from core.graphics import font

screen.fancy = False
screen.initiate((5 * 2, 9 * 2), (100, 50))
f = font.Font('C:/Users/Kosmic/Documents/PythonProjects/PRLGL/text.png')
cb = []
cf = []
draw.rect(screen.screen, Color(128, 64, 32), Rect((0, 0), (500, 500)))
msg = '123456789012345678901234567890'
for i in range(len(msg)):
    v = 256.0 / len(msg)
    cb.append(Color(int(i * v), int(i * v), int(i * v), 255))
for i in range(len(msg)):
    v = 128.0 / len(msg)
    cf.append(Color(int(192 - (i * v)), 0, int(192 - (i * v)), 255))
f.draw(screen.screen, msg, cb, cf, (0, 0))
f.drawblend(screen.screen, msg, cb, cf, (0, 1))
f.drawindent(screen.screen, len(msg), cb, (0, 2))
screen.display.update()

b = button.Button((10, 10), (12, 2), ['  Start',
                                      '       Game'], 0, None)
b.backcols = [cb, cb]
b.forecols = [cf, cf]
b.draw()

screen.display.update()

while True:
    print(end='')
