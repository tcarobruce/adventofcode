import sys
from util import readgridv, Vec as V
from collections import deque

dirs = [V(1, 0), V(0, 1), V(-1, 0), V(0, -1)]
grid = readgridv(open(sys.argv[1]))

def read_region(start):
    c = grid.get(start)
    q = deque([start])
    seen = {start}
    fence_segments = 0
    fence_lines = 0
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
            fence_segments += 1
            rot = dirs[(i + 1) % 4]
            if grid.get(pos + rot) != c or grid.get(pos + rot + d) == c:
                fence_lines += 1
    return area, fence_segments, fence_lines, seen

all_seen = set()

p1 = p2 = 0
for g in grid:
    if g in all_seen:
        continue
    area, fence_segments, fence_lines, seen = read_region(g)
    p1 += area * fence_segments
    p2 += area * fence_lines
    all_seen |= seen

print(p1)
print(p2)
