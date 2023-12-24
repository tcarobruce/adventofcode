from math import sqrt, prod
from collections import deque
from itertools import product
from operator import and_, or_
from functools import reduce, total_ordering
import re
try:
    import pyprimesieve
except ImportError:
    pass


@total_ordering
class Vec:
    def __init__(self, *els):
        self.els = els

    @property
    def dims(self):
        return len(self.els)

    def __eq__(self, other):
        return self.els == other.els

    def __lt__(self, other):
        return self.els < other.els

    def __hash__(self):
        return hash(self.els)

    def __repr__(self):
        return f"Vec({', '.join(str(el) for el in self.els)})"

    def __add__(self, other):
        assert self.dims == other.dims
        return Vec(*[(a + b) for a, b in zip(self.els, other.els)])

    def __mul__(self, scalar):
        return Vec(*[a * scalar for a in self.els])

    def __sub__(self, other):
        assert self.dims == other.dims
        return Vec(*[(a - b) for a, b in zip(self.els, other.els)])

    def distance(self, other):
        assert self.dims == other.dims
        return sqrt(sum([(a - b)**2 for a, b in zip(self.els, other.els)]))

    def rotate_cw(self):
        assert self.dims == 2
        return Vec(-self.els[1], self.els[0])

    def rotate_ccw(self):
        assert self.dims == 2
        return Vec(self.els[1], -self.els[0])

    def neighbors(self):
        assert self.dims == 2
        return [self + v for v in [Vec(1, 0), Vec(0, 1), Vec(-1, 0), Vec(0, -1)]]

    def neighbors_diag(self):
        offsets = [[d - 1, d, d + 1] for d in self.els]
        for p in product(*offsets):
            v = Vec(*p)
            if v == self:
                continue
            yield v

    @classmethod
    def extent(cls, vecs):
        vecs = iter(vecs)
        first = next(vecs)
        mins = cls(*first.els)
        maxs = cls(*first.els)
        for vec in vecs:
            mins = cls(*[min(a, b) for a, b in zip(mins.els, vec.els)])
            maxs = cls(*[max(a, b) for a, b in zip(maxs.els, vec.els)])
        return mins, maxs

    def in_extent(self, mins, maxs):
        for mi, e, ma in zip(mins.els, self.els, maxs.els):
            if not (mi <= e <= ma):
                return False
        return True


class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def dfs(self):
        yield self.value
        for child in self.children:
            yield from child.dfs()

    def bfs(self):
        q = deque([self])
        while q:
            node = q.popleft()
            yield node.value
            q.extend(node.children)


def readints(line):
    return [int(m) for m in re.findall(r"-?[\d]+", line)]


def gcd(*nums):
    factors = [dict(pyprimesieve.factorize(n)) for n in nums]
    return prod(
        pf**min(fs.get(pf, 0) for fs in factors)
        for pf in reduce(and_, (fs.keys() for fs in factors))
    )


def lcm(*nums):
    factors = [dict(pyprimesieve.factorize(n)) for n in nums]
    return prod(
        pf**max(fs.get(pf, 0) for fs in factors)
        for pf in reduce(or_, (fs.keys() for fs in factors))
    )
