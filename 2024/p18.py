import sys
from util import Vec as V, readints
from collections import deque

f = open(sys.argv[1])
coords = [V(*readints(ln)) for ln in f]


start = V(0, 0)
end = V(6, 6) if "sample" in sys.argv[1] else V(70, 70)
byte_count = 12 if "sample" in sys.argv[1] else 1024


def shortest_path(g, start):
    q = deque([(start, [])])
    seen = {start}
    while q:
        v, path = q.popleft()
        if v == end:
            return path
        for vv in v.neighbors():
            if vv not in seen and vv not in grid and vv.in_extent(start, end):
                seen.add(vv)
                q.append((vv, path + [vv]))


grid = set()
path = None
for i, v in enumerate(coords, 1):
    grid.add(v)
    if i < byte_count:
        continue
    if path is None or v in path:
        path = shortest_path(grid, start)
    if i == byte_count:
        print(len(path))
    if i > 0 and path is None:
        print(v)
        break

