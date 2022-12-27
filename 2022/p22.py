import sys
import re

lines = open(sys.argv[1]).read().splitlines()

directions = re.findall("(\d+|[LR])", lines.pop())

lines.pop()

grid = {}
minx = {}
maxx = {}
miny = {}
maxy = {}

pos = None
facing = (1, 0)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def rotate(facing, d):
    return dirs[(dirs.index(facing) + {"L": -1, "R": 1}[d]) % 4]


for y, row in enumerate(lines):
    for x, c in enumerate(row):
        if c == " ":
            continue
        if pos is None:
            pos = (x, y)
        grid[(x, y)] = c
        if y not in minx:
            minx[y] = x
        if x not in miny:
            miny[x] = y
        maxx[y] = x
        maxy[x] = y


moves = {}

def draw(grid, moves):
    for y in range(min(miny), max(maxy) + 1):
        for x in range(min(minx), max(maxx) + 1):
            c = moves.get((x, y), grid.get((x, y), " "))
            print(c, end="")
        print()


def move(pos, facing, grid):
    x, y = pos
    newx = x + facing[0]
    newy = y + facing[1]
    if newx < minx[y]:
        newx = maxx[y]
    if newy < miny[x]:
        newy = maxy[x]
    if newx > maxx[y]:
        newx = minx[y]
    if newy > maxy[x]:
        newy = miny[x]
    new_pos = (newx, newy)
    if grid[new_pos] == ".":
        pos =  new_pos
    return pos


f =  ">v<^"
for d in directions:
    if d.isdigit():
        for _ in range(int(d)):
            pos = move(pos, facing, grid)
            moves[pos] = f[dirs.index(facing)]
    else:
        facing = rotate(facing, d)
        moves[pos] = f[dirs.index(facing)]

draw(grid, moves)
col = pos[0] + 1
row = pos[1] + 1

face_score = dirs.index(facing)
print(row * 1000 + col * 4 + face_score)

# 30552, low
