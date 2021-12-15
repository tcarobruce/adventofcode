import sys
from heapq import heappop, heappush

grid = {}
for y, ln in enumerate(open(sys.argv[1])):
    for x, cost in enumerate(ln.strip()):
        grid[(x, y)] = int(cost)


def neighbors(x, y):
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1


def least_risk_path(grid):
    grid = dict(grid)
    start = (0, 0)
    dest = max([x for x, _ in grid]), max([y for _, y in grid])
    q = [(0, start, [start])]
    grid.pop(start)

    while True:
        cost, pos, chain = heappop(q)
        if pos == dest:
            #print(chain)
            return cost
        for n in neighbors(*pos):
            if n not in grid:
                continue
            heappush(q, (cost + grid.pop(n), n, chain + [n]))


# part 1: 447
print(least_risk_path(grid))

def expand_grid(grid, n=5):
    expanded = {}
    width = max([x for x, _ in grid]) + 1
    height = max([y for _, y in grid]) + 1
    for x, y in grid:
        for xoff in range(n):
            for yoff in range(n):
                nx = x + (xoff * width)
                ny = y + (yoff * height)
                expanded[(nx, ny)] = (grid[(x, y)] - 1 + xoff + yoff) % 9 + 1
    return expanded

# part 2: 2825
print(least_risk_path(expand_grid(grid)))
