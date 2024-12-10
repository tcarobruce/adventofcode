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
        return {pos}
    total = set()
    for v in pos.neighbors():
        if grid.get(v) == val + 1:
            total |= find_trails(v, val=val+1)
    return total

@cache
def find_trails2(pos, val=0):
    if val == 9:
        return 1
    total = 0
    for v in pos.neighbors():
        if grid.get(v) == val + 1:
            total += find_trails2(v, val=val+1)
    return total


print(sum([len(find_trails(th)) for th in trailheads]))
print(sum([find_trails2(th) for th in trailheads]))
