import sys
from util import Vec as V
from collections import defaultdict
from itertools import combinations

f = open(sys.argv[1])


locs = defaultdict(list)
grid = {}

for y, ln in enumerate(f):
    for x, c in enumerate(ln.strip()):
        grid[V(x, y)] = c
        if c != '.':
            locs[c].append(V(x, y))

antinodes = defaultdict(set)
antinodes2 = defaultdict(set)

for c, antennae in locs.items():
    for a, b in combinations(antennae, 2):
        v1 = b + b - a
        if grid.get(v1):
            antinodes[v1].add(c)
        v2 = a + a - b
        if grid.get(v2):
            antinodes[v2].add(c)

        v = a - b
        s = a
        while grid.get(s):
            antinodes2[s].add(c)
            s += v
        s = a
        while grid.get(s):
            antinodes2[s].add(c)
            s -= v


print(len(antinodes))
print(len(antinodes2))
