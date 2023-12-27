import sys
from util import Vec as V
from collections import deque
from functools import cache

sys.setrecursionlimit(30000)

lines = [ln.strip() for ln in open(sys.argv[1])]

G = {}
START = None
FINISH = None
DIRS = {
    ">": V(1, 0),
    "v": V(0, 1),
    "<": V(-1, 0),
    "^": V(0, -1),
}
for y, ln in enumerate(lines):
    for x, c in enumerate(ln):
        v = V(x, y)
        G[v] = c
        if c == '.' and y == 0:
            START = v
        elif c == '.' and y == len(lines) - 1:
            FINISH = v


def dfs(g, start, finish, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        visited = visited | {start}

        #print(start, len(visited))

        if start == finish:
            yield visited
        else:
            c = g.get(start)
            if c is None or c == "#":
                pass
            # elif c in DIRS:
            #     n = start + DIRS[c]
            #     yield from dfs(g, n, finish, visited)
            elif c == "." or c in DIRS:
                for n in start.neighbors():
                    yield from dfs(g, n, finish, visited)


@cache
def find_max_walk(path, finish):
    if path[-1] == finish:
        return len(path)

    m = -1
    print(len(path))
    for n in path[-1].neighbors():
        if n in path:
            continue
        c = G.get(n)
        if c in DIRS or c == ".":
            m = max(m, find_max_walk(path + (n,), finish))
    return m


def draw(g, path):
    for y, ln in enumerate(lines):
        for x, c in enumerate(ln):
            v = V(x, y)
            if v in path:
                c = "O"
            else:
                c = g[v]
            print(c, end='')
        print()

if 0:
    max_walk = 0
    for path in dfs(G, START, FINISH):
        #print(path)
        l = len(path) - 1  # steps is # of nodes - 1
        max_walk = max(max_walk, l)
        #draw(G, path)
        print(l)

    print(max_walk)

print(find_max_walk((START,), FINISH) - 1)
