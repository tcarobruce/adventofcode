import sys
from util import readgridv, Vec as V
from collections import deque

grid = readgridv(open(sys.argv[1]))

region_id = 0
regions = {}

def read_region(start):
    c = grid.get(start)
    q = deque([start])
    seen = {start}
    fences = 0
    area = 0
    while q:
        pos = q.popleft()
        area += 1
        for n in pos.neighbors():
            if n in seen:
                continue
            if grid.get(n) == c:
                seen.add(n)
                q.append(n)
            else:
                fences += 1
    return area, fences, seen

all_seen = set()

total = 0
for g in grid:
    if g in all_seen:
        continue
    area, fences, seen = read_region(g)
    total += area * fences
    all_seen |= seen

print(total)





