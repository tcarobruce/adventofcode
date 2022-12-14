import sys

G = {}
source = (500, 0)


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
            if (x, y) == source:
                print('+', end='')
                continue
            print(g.get((x, y), '.'), end='')
        print()


def pourone(g, maxy):
    x, y = source
    while True:
        if y >= maxy:
            return (x, y)
        elif (x, y + 1) not in g:
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
maxy = max([c[1] for c in G]) + 1
while True:
    d = pourone(G, maxy)
    count += 1
    G[d] = 'o'
    if d == source:
        print(count)
        break



