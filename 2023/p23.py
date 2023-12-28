import sys
from util import Vec as V
from collections import deque
from functools import cache
from itertools import count

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


def path_to_next_node(path, finish):
    neighbors = [
        n for n in path[-1].neighbors()
        if n not in path and G.get(n, "#") != "#"
    ]
    assert neighbors or path[-1] == finish, path
    if len(neighbors) > 1 or path[-1] == finish:
        return path
    return path_to_next_node(path + [neighbors[0]], finish)

def build_graph(start, finish):
    #counter = count(1)

    vertices = {start}
    edges = {}
    to_process = [start]
    processed = set()
    seen = set()
    while to_process:
        node = to_process.pop(0)
        if node in processed:
            continue
        for n in node.neighbors():
            if n in seen or G.get(n, "#") == "#":
                continue
            path = path_to_next_node([node, n], finish)
            other = path[-1]
            vertices.add(other)
            length = len(path) - 1
            edges.setdefault(node, []).append((other, length))
            edges.setdefault(other, []).append((node, length))
            seen.update(path)
            to_process.append(other)
        processed.add(node)

    return vertices, edges

V, E = build_graph(START, FINISH)

# print(E)


# @cache
# def find_max_walk(start, finish, seen):
#     if start == finish:
#         return 0

#     seen = tuple(sorted(set(seen) | {start.els}))
#     m = -1000
#     for n, cost in E[start]:
#         if n.els in seen:
#             continue
#         m = max(m, cost + find_max_walk(n, finish, seen))
#     print(start, finish, m, len(seen), find_max_walk.cache_info())
#     return m

# print(find_max_walk(START, FINISH, ()))

def dfs(start, finish, seen=None, cost=0):
    if start == finish:
        yield cost, len(seen)
    else:
        seen = (seen or set()) ^ {start}
        for n, stepcost in E[start]:
            if n in seen:
                continue
            yield from dfs(n, finish, seen=seen, cost=cost+stepcost)


m = 0
for cost, path_length in dfs(START, FINISH):
    if cost > m:
        m = cost
        print(cost, path_length)

print(m)


def bfs(start, finish):
    q = deque([([start], 0)])
    while q:
        path, cost = q.popleft()
        if path[-1] == finish:
            yield path, cost, len(q)
            continue
        for n, step_cost in E[path[-1]]:
            if n in path:
                continue
            q.append((path + [n], cost + step_cost))

m = 0
for path, cost, q_count in bfs(START, FINISH):
    if cost > m:
        m = cost
        print(cost, q_count, len(path))

print(m)



    


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

#print(find_max_walk((START,), FINISH) - 1)



# nodes = []
# for v in G:
#     if G[v] == "#":
#         continue
#     paths = len([n for n in v.neighbors() if G.get(n, "#") != "#"])
#     if paths != 2:
#         print(paths, v, G[v])
#     if paths in (3, 4):
#         nodes.append(v)

#print(len(nodes))
