import sys
from heapq import heappop, heappush

grid = {}
for y, ln in enumerate(open(sys.argv[1])):
    for x, cost in enumerate(ln.strip()):
        grid[(x, y)] = int(cost)

dest = x, y

def neighbors(x, y):
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1


def least_risk_path(start, grid, dest):
    q = [(0, start, [start])]
    grid.pop(start)
    while True:
        cost, pos, chain = heappop(q)
        if pos == dest:
            print(chain)
            return cost
        for n in neighbors(*pos):
            if n not in grid:
                continue
            heappush(q, (cost + grid.pop(n), n, chain + [n]))

print(least_risk_path((0, 0), grid, dest))
