from math import sqrt
from collections import deque
import re


class Vec:
    def __init__(self, *els):
        self.els = els

    @property
    def dims(self):
        return len(self.els)

    def __eq__(self, other):
        return self.els == other.els

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
