import sys
import re

lines = open(sys.argv[1]).read().splitlines()

path = re.findall(r"(\d+|[LR])", lines.pop())
lines.pop()

grid = {}
warp = {}
ymins = {}
ymaxs = {}

pos = None
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
facing = directions[0]

for y, row in enumerate(lines, 1):
    first = None
    for x, c in enumerate(row, 1):
        if c == " ":
            continue
        if first is None:
            first = (x, y)
            if pos is None:
                pos = first
        grid[(x, y)] = c
        ymins[x] = min(ymins.get(x, 1000000), y)
        ymaxs[x] = max(ymaxs.get(x, -1000000), y)
    last = (x, y)
    warp[(first[0] - 1, first[1])] = last
    warp[(last[0] + 1, last[1])] = first

for x in ymins:
    first = (x, ymins[x])
    last = (x, ymaxs[x])
    warp[(first[0], first[1] - 1)] = last
    warp[(last[0], last[1] + 1)] = first


def advance(pos, facing):
    new_pos = (pos[0] + facing[0], pos[1] + facing[1])
    new_pos = warp.get(new_pos, new_pos)
    dest = grid[new_pos]
    if dest == ".":
        pos = new_pos
    elif dest == "#":
        pass
    else:
        assert False, "Unknown dest %s at %s" % (dest, new_pos)

    return pos

def rotate(p, facing):
    offset = {"L": -1, "R": 1}[p]
    return directions[(directions.index(facing) + offset) % 4]

for p in path:
    if p.isdigit():
        for _ in range(int(p)):
            pos = advance(pos, facing)
    else:
        facing = rotate(p, facing)

print(pos, facing)
col, row = pos
print(1000 * row + 4 * col + directions.index(facing))
