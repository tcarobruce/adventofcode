import sys
from util import Vec as V
from collections import deque
from functools import cache

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

        print(start, len(visited))

        if start == finish:
            yield len(visited)
        else:
            #print(start, len(visited))

            c = g.get(start)
            if c is None or c == "#":
                pass
            elif c == ".":
                for n in start.neighbors():
                    yield from dfs(g, n, finish, visited)
            elif c in DIRS:
                yield from dfs(g, start + DIRS[c], finish, visited | {start + DIRS[c]})

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
            while c in DIRS:
                start = start + DIRS[c]
                visited = visited | {start}
                c = g.get(start)
            if c is None or c == "#":
                pass
            elif c == ".":
                for n in start.neighbors():
                    yield from dfs(g, n, finish, visited)


def find_all_paths(g, start, finish):
    q = deque([[start]])

    while q:
        path = q.popleft()
        last = path[-1]
        if last == finish:
            yield path
        else:
            for node in last.neighbors():
                if node in path:
                    continue
                c = g.get(node)
                if c is None or c == "#":
                    continue
                if c in DIRS:
                    q.append(path + [node, node + DIRS[c]])
                if c == ".":
                    q.append(path + [node])


max_walk = 0
for path in dfs(G, START, FINISH):
    print(path)
    l = len(path)
    max_walk = max(max_walk, l)
    print(l)

print(max_walk)
