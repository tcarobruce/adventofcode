import sys
import re

lines = open(sys.argv[1]).read().splitlines()

path = re.findall(r"(\d+|[LR])", lines.pop())
lines.pop()

grid = {}
warp = {}
ymins = {}
ymaxs = {}

orig_pos = None
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for y, row in enumerate(lines, 1):
    first = None
    for x, c in enumerate(row, 1):
        if c == " ":
            continue
        if first is None:
            first = (x, y)
            if orig_pos is None:
                orig_pos = first
        grid[(x, y)] = c
        ymins[x] = min(ymins.get(x, 1000000), y)
        ymaxs[x] = max(ymaxs.get(x, -1000000), y)
    last = (x, y)
    warp[(first, (-1, 0))] = last, None
    warp[(last, (1, 0))] = first, None

for x in ymins:
    first = (x, ymins[x])
    last = (x, ymaxs[x])
    warp[(first, (0, -1))] = last, None
    warp[(last, (0, 1))] = first, None

def advance(pos, facing):
    warped = warp.get((pos, facing))
    if warped is None:
        new_pos = pos[0] + facing[0], pos[1] + facing[1]
        turn = None
    else:
        new_pos, turn = warped
    dest = grid[new_pos]
    if dest == ".":
        pos = new_pos
        if turn:
            facing = rotate(turn, facing)
    elif dest == "#":
        pass
    else:
        assert False, "Unknown dest %s at %s" % (dest, new_pos)

    return pos, facing

def rotate(p, facing):
    offset = {"L": -1, "R": 1, "O": 2}[p]
    return directions[(directions.index(facing) + offset) % 4]

def draw(*a):
    pass

def run_path(pos, facing):
    for p in path:
        if p.isdigit():
            for _ in range(int(p)):
                new_pos, facing = advance(pos, facing)
                if new_pos == pos:
                    break
                pos = new_pos
                draw(pos, facing)
        else:
            facing = rotate(p, facing)
            draw(pos, facing)
    return pos, facing

pos, facing = run_path(orig_pos, directions[0])
print(pos, facing)
col, row = pos
print(1000 * row + 4 * col + directions.index(facing))

warp = {}

def zip_edges(a, adir, aturn, b, bdir, bturn):
    for apos, bpos in zip(a, b):
        warp[(apos, adir)] = bpos, aturn
        warp[(bpos, bdir)] = apos, bturn

moves = {}
f =  ">v<^"
minx = min(grid)[0]
maxx = max(grid)[0]
ys = [g[1] for g in grid]
miny = min(ys)
maxy = max(ys)

def draw(pos, facing):
    moves[pos] = f[directions.index(facing)]
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            c = moves.get((x, y), grid.get((x, y), " "))
            print(c, end="")
        print()
    input()

if sys.argv[1] == "p22_test.txt":
    zip_edges(
        [(9, y) for y in range(1, 5)], (-1, 0), "L",  # 1L
        [(x, 5) for x in range(5, 9)], (0, -1), "R",  # 3T
    )
    zip_edges(
        [(9, y) for y in range(9, 13)], (-1, 0), "R", # 3B
        [(x, 8) for x in reversed(range(5, 9))], (0, -1), "L",  # 5L
    )
    zip_edges(
        [(12, y) for y in reversed(range(5, 9))], (1, 0), "R",  # 4R
        [(x, 9) for x in range(13, 17)], (0, -1), "L",  # 6T
    )
    zip_edges(
        [(x, 1) for x in range(9, 13)], (0, -1), "O",  # 1T
        [(x, 5) for x in reversed(range(1, 5))], (0, -1), "O",  # 2T
    )
    zip_edges(
        [(x, 8) for x in reversed(range(1, 5))], (0, 1), "O",  # 2B
        [(x, 12) for x in range(9, 13)], (0, 1), "O",  # 5B
    )
    zip_edges(
        [(12, y) for y in range(1, 5)], (1, 0), "O",  # 1R
        [(16, y) for y in reversed(range(9, 13))], (1, 0), "O",  # 6R
    )
    zip_edges(
        [(x, 12) for x in reversed(range(13, 17))], (0, 1), "L",  # 6B
        [(1, y) for y in range(5, 9)], (-1, 0), "R",  # 2L
    )


pos, facing = run_path(orig_pos, directions[0])
print(pos, facing)
col, row = pos
print(1000 * row + 4 * col + directions.index(facing))
