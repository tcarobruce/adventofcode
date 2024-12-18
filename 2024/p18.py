import sys
from util import Vec as V, readints
from collections import deque

f = open(sys.argv[1])
coords = [V(*readints(ln)) for ln in f]


start = V(0, 0)
end = V(6, 6) if "sample" in sys.argv[1] else V(70, 70)

grid = set()
for i, v in enumerate(coords, 1):
    grid.add(v)

    if i == 1024:
        break


def shortest_path(g, start):
    q = deque([(start, 0)])
    seen = {start}
    while True:
        v, steps = q.popleft()
        print(steps, len(q), len(seen))
        if v == end:
            return steps
        for vv in v.neighbors():
            if vv not in seen and vv not in grid and vv.in_extent(start, end):
                seen.add(vv)
                q.append((vv, steps + 1))

print(shortest_path(grid, start))
