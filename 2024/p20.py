import sys

from util import Vec as V, readgridv
from heapq import heappop, heappush
from functools import cache
from collections import Counter

grid = readgridv(open(sys.argv[1]).read().split())

start = [v for v, c in grid.items() if c == 'S'][0]
end = [v for v, c in grid.items() if c == 'E'][0]


def find_paths():
    paths = {}
    q = [(0, end, [])]

    while q:
        dist, pos, path = heappop(q)
        paths[pos] = path
        for n in pos.neighbors():
            if n in paths:
                continue
            c = grid.get(n)
            if c and c in '.S':
                heappush(q, (dist + 1, n, [n] + path))
    return paths

paths = find_paths()
mainline = paths[start]
distances = {pos: len(path) for pos, path in paths.items()}
nocheat = distances[start]

dirs = [V(2, 0), V(0, 2), V(-2, 0), V(0, -2)]

ct = Counter()
for pos in mainline:
    for d in dirs:
        n = pos + d
        c = grid.get(n)
        if c and c in '.E':
            l = distances[n] + (nocheat - distances[pos]) + 2
            if l < nocheat:
                ct[nocheat - l] += 1


t = 0
for savings, count in sorted(ct.items()):
    print(count, savings)
    if savings >= 100:
        t += count
print(t)







