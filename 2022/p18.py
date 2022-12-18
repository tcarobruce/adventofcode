import sys
from itertools import product

lines = open(sys.argv[1]).read().splitlines()
cubes = [tuple([int(c) for c in ln.split(",")]) for ln in lines]


def neighbors(c):
    x, y, z = c
    yield (x - 1, y, z)
    yield (x + 1, y, z)
    yield (x, y - 1, z)
    yield (x, y + 1, z)
    yield (x, y, z - 1)
    yield (x, y, z + 1)


def add_cubes(g, cubes):
    total = 0
    for cube in cubes:
        total += 6
        for n in neighbors(cube):
            if n in g:
                total -= 2
        g.add(cube)
    return total

G = set()
total = add_cubes(G, cubes)
print(total)

ranges = [(min(c[i] for c in G), max(c[i] for c in G)) for i in range(3)]


def find_bubble(n):
    q = [n]
    seen = set()
    while q:
        c = q.pop(0)
        if c in G or c in seen:
            continue
        seen.add(c)
        for i, (mind, maxd) in enumerate(ranges):
            if c[i] < mind or c[i] > maxd:
                return set()
        q.extend(neighbors(c))
    return seen


bubbles = set()
for c in product(*[range(*r) for r in ranges]):
    if c not in G and c not in bubbles:
        bubbles |= find_bubble(c)


print(total + add_cubes(G, bubbles))
