import sys
from util import Vec as V

f = open(sys.argv[1])

by_coord = (
    ((x, y), c)
    for y, ln in enumerate(f)
    for x, c in enumerate(ln.strip())
)
grid = {}
START = None
DIRECTION = V(0, -1)

for (x, y), c in by_coord:
    if c == '^':  # only this char is used for starting position
        START = V(x, y)
        c = '.'
    grid[V(x, y)] = c


def walk(start, direction):
    seen = {(start, direction)}
    position = start
    while True:
        next_position = position + direction
        c = grid.get(next_position)
        if (next_position, direction) in seen:
            return seen, True
        elif c is None:
            return seen, False
        elif c == '#':
            direction = direction.rotate_cw()
        elif c == '.':
            position = next_position
            seen.add((next_position, direction))
        else:
            raise Exception("Bad place %s at %s!" % (next_position, c))

visited, loop = walk(START, DIRECTION)
positions = set([v[0] for v in visited])
ct = len(positions)
print(ct)

tot = 0
for i, pos in enumerate(positions, 1):
    print(f"{i}/{ct}")
    assert grid[pos] == '.'
    grid[pos] = '#'
    _, loop = walk(START, DIRECTION)
    if loop:
        tot += 1
    grid[pos] = '.'

print(tot)


