import sys
from util import readgridv, Vec as V
from collections import deque

grid = readgridv(open(sys.argv[1]))

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

dirs = [V(1, 0), V(0, 1), V(-1, 0), V(0, -1)]

def read_region2(start):
    c = grid.get(start)
    q = deque([start])
    seen = {start}
    fences = 0
    area = 0
    while q:
        pos = q.popleft()
        area += 1
        for i, d in enumerate(dirs):
            n = pos + d
            if n in seen:
                continue
            if grid.get(n) == c:
                seen.add(n)
                q.append(n)
                continue

            rot = dirs[(i + 1) % 4]
            if grid.get(pos + rot) != c or grid.get(pos + rot + d) == c:
                fences += 1

    return area, fences, seen

all_seen = set()

total = 0
for g in grid:
    if g in all_seen:
        continue
    area, fences, seen = read_region2(g)
    total += area * fences
    all_seen |= seen

print(total)
