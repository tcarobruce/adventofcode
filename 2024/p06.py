import sys
from util import Vec as V

f = open(sys.argv[1])

by_coord = (
    ((x, y), c)
    for y, ln in enumerate(f)
    for x, c in enumerate(ln.strip())
)
grid = {}
start = None
direction = V(0, -1)

for (x, y), c in by_coord:
    grid[V(x, y)] = c
    if c == '^':  # only this char is used for starting position
        start = V(x, y)


def walk(start, direction):
    seen = {start}
    position = start
    while True:
        next_position = position + direction
        c = grid.get(next_position)
        if c is None:
            return seen
        elif c == '#':
            direction = direction.rotate_cw()
        else:
            position = next_position
            seen.add(next_position)

visited = walk(start, direction)
print(visited)
print(len(visited))
