import sys
from itertools import cycle

jet = lambda i: "< >".index(i) - 1
jets = cycle(open(sys.argv[1]).read().strip())
width = 7

raw_rocks = [r.split() for r in """
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
""".strip().split("\n\n")]

rocks = []
for rr in raw_rocks:
    rock = []
    for yoff, row in enumerate(reversed(rr)):
        for xoff, c in enumerate(row):
            if c == ".":
                continue
            rock.append((xoff, yoff))
    rocks.append(rock)

rocks = cycle(rocks)


G = {(i, 0) for i in range(7)}

def collision(pos, rock, grid):
    # pos is always lower left
    x, y = pos
    if x < 0:
        return True
    w = max([r[0] for r in rock]) + 1
    if x + w > 7:
        return True
    for xoff, yoff in rock:
        if (x + xoff, y + yoff) in grid:
            return True
    return False


def draw(grid, rock, pos):
    r = set()
    x, y = pos
    for xoff, yoff in rock:
        r.add((x + xoff, y + yoff))
    for y in range(height + 4, -1, -1):
        print("%03d" % y, end='')
        print('|', end='')
        for x in range(7):
            c = '.'
            if (x, y) in r:
                c = "@"
            elif (x, y) in grid:
                c = "#"
            print(c, end="")
        print('|')




height = 0
dbg = 0
for _ in range(2022):
    rock = next(rocks)
    x, y = 2, height + 4
    if dbg:
        print('-' * 40)
        print(height)
        draw(G, rock, (x, y)); input()

    while True:
        xoff = jet(next(jets))
        if not collision((x + xoff, y), rock, G):
            x += xoff
        if dbg:
            print(xoff)
            draw(G, rock, (x, y)); input()
        if collision((x, y - 1), rock, G):
            height = max(height, y + max([r[1] for r in rock]))
            for xoff, yoff in rock:
                G.add((x + xoff, y + yoff))
            break
        else:
            y -= 1
        if dbg:
            draw(G, rock, (x, y)); input()

print(height)
