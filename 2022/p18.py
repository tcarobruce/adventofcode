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

minx, maxx = min([c[0] for c in G]), max([c[0] for c in G])
miny, maxy = min([c[1] for c in G]), max([c[1] for c in G])
minz, maxz = min([c[2] for c in G]), max([c[2] for c in G])


def touches_outside(n):
    q = [n]
    seen = set()
    while q:
        c = q.pop(0)
        if c in G or c in seen:
            continue
        seen.add(c)
        if c[0] < minx or c[0] > maxx:
            return True
        if c[1] < miny or c[1] > maxy:
            return True
        if c[2] < minz or c[2] > maxz:
            return True
        q.extend(neighbors(c))
    return False


bubbles = []
for x in range(minx, maxx + 1):
    for y in range(miny, maxy + 1):
        for z in range(minz, maxz + 1):
            c = (x, y, z)
            if c not in G and not touches_outside(c):
                bubbles.append(c)

for b in bubbles:
    total += 6
    for n in neighbors(b):
        if n in G:
            total -= 2
    G.add(b)
print(total)
