import sys
from dataclasses import dataclass, astuple, asdict
from collections import Counter
from itertools import chain


@dataclass(frozen=True)
class Cuboid:
    xmin: int
    xmax: int
    ymin: int
    ymax: int
    zmin: int
    zmax: int

    def size(self):
        return (
            (self.xmax - self.xmin + 1)
            * (self.ymax - self.ymin + 1)
            * (self.zmax - self.zmin + 1)
        )

    def isinit(self):
        return (
            abs(self.xmin) <= 50
            and abs(self.ymin) <= 50
            and abs(self.zmin) <= 50
            and abs(self.xmax) <= 51
            and abs(self.ymax) <= 51
            and abs(self.zmax) <= 51
        )

    def __and__(self, other):
        new = []
        tups = zip(astuple(self), astuple(other))
        for _ in "xyz":
            dmin = max(next(tups))
            dmax = min(next(tups))
            if dmin >= dmax:
                return Empty
            new.extend([dmin, dmax])
        return Cuboid(*new)


Empty = Cuboid(0, -1, 0, -1, 0, -1)

cuboids = []
for line in open(sys.argv[1]):
    state, coords = line.strip().split(" ")
    state = state == "on"
    dims = []
    for t in coords.split(","):
        dmin, dmax = t[2:].split("..")
        dims.extend([int(dmin), int(dmax)])
    cuboids.append((state, Cuboid(*dims)))


# significant inspiration from https://github.com/Bruception/advent-of-code-2021/blob/main/day22/part2.py
def ignite_reactor(cuboids, init_area=False):
    processed = Counter()
    for state, cuboid in cuboids:
        if init_area and not cuboid.isinit():
            continue

        intersects = Counter({cuboid: state} if state else {})

        for other, value in processed.items():
            intersect = cuboid & other
            if intersect != Empty:
                intersects[intersect] -= value
        processed.update(intersects)

    print(len(processed))
    return sum(p.size() * value for p, value in processed.items())


print(ignite_reactor(cuboids, init_area=True))
print(ignite_reactor(cuboids))

