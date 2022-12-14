import sys

G = {}


for ln in open(sys.argv[1]):
    lx, ly = None, None
    coords = ln.strip().split(" -> ")
    for coord in coords:
        sx, sy = [int(c) for c in coord.split(",")]
        if lx is not None:
            for x in range(min(sx, lx), max(sx, lx) + 1):
                for y in range(min(sy, ly), max(sy, ly) + 1):
                    G[(x, y)] = "#"
        lx, ly = sx, sy


def draw(g):
    minx = min(g)[0]
    maxx = max(g)[0]
    ys = [c[1] for c in g]
    miny = 0
    maxy = max(ys)
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if (x, y) == (500, 0):
                print('+', end='')
                continue
            print(g.get((x, y), '.'), end='')
        print()



def pourone(g):
    x, y = 500, 0
    maxy = max([c[1] for c in g])
    while True:
        if y > maxy:
            return None
        if (x, y + 1) not in g:
            y += 1
        elif (x - 1, y + 1) not in g:
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in g:
            x += 1
            y += 1
        else:
            return (x, y)

count = 0
while True:
    d = pourone(G)
    if d is None:
        print(count)
        break
    count += 1
    G[d] = 'o'



