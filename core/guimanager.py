registered = {}
visible = []
curid = -1


def register(g):
    global curid
    curid += 1
    registered[curid] = g
    return curid


def setdrawing(vis, guiid):
    if guiid in registered.keys():
        cg = guiid in visible
        if vis and not cg:
            visible.append(guiid)
        elif not vis and cg:
            visible.remove(guiid)


def draw():
    for g in visible:
        cdg = registered[g]
        cdg.draw()
