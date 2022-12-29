import sys
from collections import defaultdict

lines = open(sys.argv[1]).read().splitlines()

elves = set()
for y, row in enumerate(lines):
    for x, c in enumerate(row):
        if c == "#":
            elves.add((x, y))

moves = [
    [(-1, -1), (0, -1), (1, -1)],
    [(-1, 1), (0, 1), (1, 1)],
    [(-1, -1), (-1, 0), (-1, 1)],
    [(1, -1), (1, 0), (1, 1)],
]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def has_neighbors(pos, grid):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if add(pos, (x, y)) in grid:
                return True
    return False


def round(i, grid, moves):
    i = i % len(moves)
    round_moves = moves[i:] + moves[:i]
    proposals = defaultdict(set)
    for pos in grid:
        if not has_neighbors(pos, grid):
            proposals[pos].add(pos)
        else:
            for m in round_moves:
                if not any(add(pos, md) in grid for md in m):
                    proposals[add(pos, m[1])].add(pos)
                    break
            else:
                proposals[pos].add(pos)

    new_grid = set()
    for dest, origins in proposals.items():
        if len(origins) == 1:
            new_grid.add(dest)
        else:
            new_grid.update(origins)
    return new_grid


def ranges(grid):
    minx = miny = 1000000
    maxx = maxy = -1000000
    for n in grid:
        minx = min(minx, n[0])
        maxx = max(maxx, n[0])
        miny = min(miny, n[1])
        maxy = max(maxy, n[1])
    return (minx, maxx), (miny, maxy)


def draw(grid):
    xs, ys = ranges(grid)
    for y in range(ys[0], ys[1] + 1):
        for x in range(xs[0], xs[1] + 1):
            c = "#" if (x, y) in grid else "."
            print(c, end="")
        print()


draw(elves)
print()
for i in range(10):
    elves = round(i, elves, moves)
    draw(elves)
    print()
    #input()

xs, ys = ranges(elves)
print((xs[1] + 1 - xs[0]) * (ys[1] + 1 - ys[0]) - len(elves))
