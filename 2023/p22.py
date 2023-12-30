import sys
from util import readints, Vec as V
from string import ascii_uppercase
from collections import Counter
#from functools import cache
from heapq import heappop, heappush

lines = [ln.strip() for ln in open(sys.argv[1])]

BRICKS = {}
for i, line in enumerate(lines, 1):
    ints = readints(line)
    a, b = V.extent([V(*ints[:3]), V(*ints[3:])])
    #b = b + V(1, 1, 1)  # make interval open on right
    if len(lines) < 26:
        i = ascii_uppercase[i-1]
    BRICKS[i] = (a, b)


def ranges_overlap(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])


def overlap_xy(a, b, dims=[0, 1]):
    a = BRICKS[a]
    b = BRICKS[b]
    return all(
        ranges_overlap((a[0].els[i], a[1].els[i]), (b[0].els[i], b[1].els[i]))
        for i in dims
    )


def drop(terrain, dependencies, brick):
    floor = 0
    for alt, bricks in sorted(terrain.items(), reverse=True):
        overlaps = [b for b in bricks if overlap_xy(brick, b)]
        if overlaps:
            dependencies[brick] = overlaps
            floor = alt
            break

    b = BRICKS[brick]
    offset = V(0, 0, b[0].els[2] - floor - 1)
    bottom, top = BRICKS[brick]
    BRICKS[brick] = (bottom - offset, top - offset)
    terrain.setdefault(BRICKS[brick][1].els[2], []).append(brick)


def drop_many(bricks):
    terrain = {}  # a list of lists of bricks, ordered by descending height
    dependencies = {}

    # drop starting with closest to the ground
    by_height = sorted(bricks, key=lambda b: bricks[b][0].els[2])
    for brick in by_height:
        drop(terrain, dependencies, brick)

    return terrain, dependencies


terrain, dependencies = drop_many(BRICKS)

disintegratable = set(BRICKS)
for deps in dependencies.values():
    if len(deps) == 1:
        disintegratable.discard(deps[0])

print(len(disintegratable))

supports = {}
for depender, supporters in dependencies.items():
    for supporter in supporters:
        supports.setdefault(supporter, []).append(depender)

def chain_reaction(brick):
    orig = brick
    falling = set()
    q = [(BRICKS[brick][0].els[2], brick)]
    while q:
        #print(len(q), q)
        _, brick = heappop(q)
        if brick != orig and set(dependencies.get(brick, [])) - falling:
            # still supported
            continue
        falling.add(brick)
        for dep in supports.get(brick, []):
            heappush(q, (BRICKS[dep][0].els[2], dep))
    return falling - {orig}


print(sum([len(chain_reaction(b)) for b in BRICKS]))
