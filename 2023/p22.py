import sys
from util import readints, Vec as V
from string import ascii_uppercase
from collections import Counter
from functools import cache

lines = [ln.strip() for ln in open(sys.argv[1])]

BRICKS = {}
for i, line in enumerate(lines, 1):
    ints = readints(line)
    a, b = V.extent([V(*ints[:3]), V(*ints[3:])])
    #b = b + V(1, 1, 1)  # make interval open on right
    #i = ascii_uppercase[i-1]
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


def height(brick):
    brick = BRICKS[brick]
    return brick[1].els[2] - brick[0].els[2] + 1


def drop(terrain, dependencies, brick):
    new_h = height(brick)
    for alt, bricks in sorted(terrain.items(), reverse=True):
        overlaps = [b for b in bricks if overlap_xy(brick, b)]
        if overlaps:
            dependencies[brick] = overlaps
            new_h += alt
            break
    terrain.setdefault(new_h, []).append(brick)


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

print(dependencies)
print(supports)

@cache
def _chain_reaction(brick, falling_t=None):
    if falling_t is None:
        falling_t = ()
    falling = set(falling_t) | {brick}
    new_falling = set()
    for dep in supports.get(brick, []):
        if not set(dependencies[dep]) - falling:
            new_falling.add(dep)
    if new_falling:
        falling.update(new_falling)
        falling_t = tuple(sorted(falling))
        for dep in new_falling:
            falling.update(_chain_reaction(dep, falling_t=falling_t))
    return falling

def chain_reaction_length(brick):
    return len(_chain_reaction(brick) - {brick})


print(sum([chain_reaction_length(b) for b in BRICKS]))
