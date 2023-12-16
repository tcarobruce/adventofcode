import sys
from util import Vec as V

lines = [ln.strip() for ln in open(sys.argv[1])]

MIRRORS = {
    "/": {
        V(1, 0): V(0, -1),
        V(-1, 0): V(0, 1),
        V(0, 1): V(-1, 0),
        V(0, -1): V(1, 0),
    },
    "\\": {
        V(1, 0): V(0, 1),
        V(-1, 0): V(0, -1),
        V(0, 1): V(1, 0),
        V(0, -1): V(-1, 0),
    },
}
SPLITTERS = {
    "|": {
        V(1, 0): [V(0, -1), V(0, 1)],
        V(-1, 0): [V(0, -1), V(0, 1)],
        V(0, 1): [V(0, 1)],
        V(0, -1): [V(0, -1)],
    },
    "-": {
        V(1, 0): [V(1, 0)],
        V(-1, 0): [V(-1, 0)],
        V(0, 1): [V(1, 0), V(-1, 0)],
        V(0, -1): [V(1, 0), V(-1, 0)],
    },
}

beams = [(V(0, 0), V(1, 0))]

energized = set()
seen = set()

while beams:
    position, velocity = beams.pop(0)
    if (position, velocity) in seen:
        continue
    if position.els[0] < 0 or position.els[0] >= len(lines[0]):
        continue
    if position.els[1] < 0 or position.els[1] >= len(lines):
        continue
    seen.add((position, velocity))
    energized.add(position)
    c = lines[position.els[1]][position.els[0]]
    #print(c, position, velocity)
    if c == ".":
        beams.append((position + velocity, velocity))
    elif c in MIRRORS:
        velocity = MIRRORS[c][velocity]
        beams.append((position + velocity, velocity))
    elif c in SPLITTERS:
        for nv in SPLITTERS[c][velocity]:
            beams.append((position + nv, nv))
    #print(beams, len(energized))

print(len(energized))
