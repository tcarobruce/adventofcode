import sys
from util import Vec as V, readints
from collections import deque

f = open(sys.argv[1])
coords = [V(*readints(ln)) for ln in f]


start = V(0, 0)
end = V(6, 6) if "sample" in sys.argv[1] else V(70, 70)
byte_count = 12 if "sample" in sys.argv[1] else 1024


def shortest_path(g, start):
    q = deque([(start, 0)])
    seen = {start}
    while q:
        v, steps = q.popleft()
        if v == end:
            return steps
        for vv in v.neighbors():
            if vv not in seen and vv not in grid and vv.in_extent(start, end):
                seen.add(vv)
                q.append((vv, steps + 1))


grid = set()
for i, v in enumerate(coords, 1):
    grid.add(v)
    s = shortest_path(grid, start)
    if i == byte_count:
        print(s)
    if s is None:
        print(v)
        break

