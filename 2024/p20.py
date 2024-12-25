import sys

from util import Vec as V, readgridv
from heapq import heappop, heappush
from functools import cache
from collections import Counter, deque

grid = readgridv(open(sys.argv[1]).read().split())

start = [v for v, c in grid.items() if c == 'S'][0]
end = [v for v, c in grid.items() if c == 'E'][0]


def find_distances(start):
    distances = {start: 0}
    q = [(0, start)]

    while q:
        dist, pos = heappop(q)
        for n in pos.neighbors():
            if n in distances:
                continue
            c = grid.get(n)
            if c and c in '.SE':
                heappush(q, (dist + 1, n))
                distances[n] = dist + 1
    return distances

to_end = find_distances(end)
from_start = find_distances(start)


def manhattan_range(pos, radius):
    for xoff in range(-radius, radius + 1):
        for yoff in range(-radius + abs(xoff), radius - abs(xoff) + 1):
            yield pos + V(xoff, yoff), abs(xoff) + abs(yoff)


def find_cheats(cheats):
    seen = {start}
    q = [(0, start)]
    max_dist = to_end[start]
    while q:
        dist, pos = heappop(q)
        print(dist, '/', max_dist)
        if dist >= max_dist:
            break

        for cheat_dest, cheat_dist in manhattan_range(pos, cheats):
            c = grid.get(cheat_dest)
            if c and c in '.E':
                saved = to_end[pos] - cheat_dist - to_end[cheat_dest]
                if saved > 0:
                    yield saved

        for n in pos.neighbors():
            if n in seen:
                continue
            seen.add(n)
            c = grid.get(n)
            if c in '.E':
                heappush(q, (dist + 1, n))

tot = 0
for k, v in sorted(Counter(find_cheats(2)).items()):
    print(v, k)
    if k >= 100:
        tot += v
print(tot)

lim = 50 if 'sample' in sys.argv[1] else 100

tot = 0
for k, v in sorted(Counter(find_cheats(20)).items()):
    if k >= lim:
        print(v, k)
        tot += v
print(tot)
