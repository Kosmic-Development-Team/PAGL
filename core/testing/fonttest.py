from core import screen
from core.textures import font
from pygame import draw
from pygame import Rect
from pygame import Color

screen.initiate((20, 10), (25, 50))
f = font.Font('C:/Users/Kosmic/Documents/PythonProjects/PRLGL/text.png')
cb = []
cf = []
draw.rect(screen.screen, Color(128, 64, 32), Rect((0, 0), (500, 500)))
msg = 'Hello'
for i in range(len(msg)):
    v = 256.0 / len(msg)
    cb.append(Color(int(i * v), int(i * v), int(i * v), 255))
for i in range(len(msg)):
    v = 256.0 / len(msg)
    cf.append(Color(0, int(255 - (i * v)), 0, 255))
f.drawfull(screen.screen, msg, cb, cf, (0, 0))
screen.display.update()
while True:
    print(end='')
