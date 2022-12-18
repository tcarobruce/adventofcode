import sys
from itertools import cycle, count

jet = lambda i: "< >".index(i) - 1
jets = open(sys.argv[1]).read().strip()
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


def drop_rocks(rocks, jets):
    rocks = cycle(enumerate(rocks))
    jets = cycle(enumerate(jets))
    G = {(i, 0) for i in range(7)}
    height = 0

    for rock_count in count(1):
        ri, rock = next(rocks)
        x, y = 2, height + 4

        while True:
            ji, j = next(jets)
            xpush = jet(j)
            if not collision((x + xpush, y), rock, G):
                x += xpush
            if collision((x, y - 1), rock, G):
                height = max(height, y + max([r[1] for r in rock]))
                for xoff, yoff in rock:
                    G.add((x + xoff, y + yoff))
                break
            else:
                y -= 1
        yield rock_count, ri, ji, height


def find_cycle(rocks, jets):
    cycles = {}
    last_landed = False
    for rock_count, ri, ji, height in drop_rocks(rocks, jets):
        k = ri, ji
        cycles.setdefault(k, []).append((rock_count, height))
        ck = cycles[k]
        if len(ck) >= 4:
            diffs = {(a[0] - b[0], a[1] - b[1]) for a, b in zip(ck[-3:], ck[-4:-1])}
            if len(diffs) == 1:
                return ck[-4] + diffs.pop()


def height_after_cycles_naive(rocks, jets, n):
    for rock_count, _, _, height in drop_rocks(rocks, jets):
        if rock_count >= n:
            return height


def height_after_cycles(rocks, jets, n):
    start_count, start_height, interval_count, interval_height = find_cycle(rocks, jets)
    intervals, remainder = divmod(n - start_count, interval_count)

    return intervals * interval_height + height_after_cycles_naive(rocks, jets, start_count + remainder)


print(height_after_cycles(rocks, jets, 2022))
print(height_after_cycles(rocks, jets, 1000000000000))
