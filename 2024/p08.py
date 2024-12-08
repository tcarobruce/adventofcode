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

for c, antennae in locs.items():
    for a, b in combinations(antennae, 2):
        v1 = b + b - a
        if grid.get(v1):
            antinodes[v1].add(c)
        v2 = a + a - b
        if grid.get(v2):
            antinodes[v2].add(c)

print(len(antinodes))
#print(antinodes)
