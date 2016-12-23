from randoms.maze import maze
from core import screen
from core.graphics import font
from pygame import Color
from pygame import display

screen.fancy = False
screen.initiate((4, 4), (200, 200))
f = font.Font('C:/Users/Kosmic/Documents/PythonProjects/PRLGL/pixels.png')
maxc = 1


def itnation():
    global maxc
    mz = maze.mazy
    cmz = []
    if maze.threads > maxc:
        maxc = maze.threads
    for i in range(200):
        cmz.append([])
        for j in range(200):
            k = mz[i][j]
            if k:
                col = Color(0, 0, 0, 0)
                l = int((k * 360.0) / maxc)

                if l > 360:
                    l = 360
                col.hsva = (l, 99, 99, 99)
                cmz[i].append(col)
            else:
                cmz[i].append(Color(0, 0, 0, 255))

    for k in range(200):
        f.drawindent(screen.screen, 200, cmz[k], (0, k))

    display.update()

maze.start(itnation)
print('DONE')
while True:
    1 == 1
