from util import Vec as V
import sys
from functools import cache


grid = {}
trailheads = []
for y, ln in enumerate(open(sys.argv[1])):
    for x, c in enumerate(ln.strip()):
        coord = V(x, y)
        grid[coord] = int(c)
        if int(c) == 0:
            trailheads.append(coord)


@cache
def find_trails(pos, val=0):
    if val == 9:
        return [pos]
    total = []
    for v in pos.neighbors():
        if grid.get(v) == val + 1:
            total.extend(find_trails(v, val=val+1))
    return total


trails = [find_trails(th) for th in trailheads]

print(sum([len(set(t)) for t in trails]))
print(sum([len(t) for t in trails]))
