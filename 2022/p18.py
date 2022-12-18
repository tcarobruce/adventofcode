import sys

lines = open(sys.argv[1]).read().splitlines()

G = set()

total = 0

def neighbors(c):
    x, y, z = c
    yield (x - 1, y, z)
    yield (x + 1, y, z)
    yield (x, y - 1, z)
    yield (x, y + 1, z)
    yield (x, y, z - 1)
    yield (x, y, z + 1)

for ln in lines:
    cube = tuple([int(c) for c in ln.split(",")])
    total += 6
    for n in neighbors(cube):
        if n in G:
            total -= 2
    G.add(cube)

print(total)
