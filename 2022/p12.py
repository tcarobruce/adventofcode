import sys
from heapq import heappop, heappush

grid = {}
start = end = None
for y, line in enumerate(open(sys.argv[1]).read().splitlines()):
    for x, c in enumerate(line):
        if c == "S":
            start = (x, y)
            c = 'a'
        elif c == "E":
            end = (x, y)
            c = 'z'
        grid[(x, y)] = ord(c) - ord('a')


q = [(0, start)]
visited = set(start)

def neighbors(pos):
    x, y = pos
    yield (x - 1, y)
    yield (x, y - 1)
    yield (x + 1, y)
    yield (x, y + 1)


while True:
    steps, pos = heappop(q)
    if pos == end:
        print(steps)
        break

    height = grid[pos]

    for n in neighbors(pos):
        if n in visited:
            continue
        nheight = grid.get(n)
        if nheight is None:  # outside grid
            continue
        if nheight - height > 1:
            continue
        visited.add(n)
        heappush(q, (steps + 1, n))
