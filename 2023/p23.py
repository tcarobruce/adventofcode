import sys
from util import Vec as V


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


def path_to_next_node(path, finish, dirs={-1, 1}):
    last = path[-1]
    neighbors = [
        n for n in last.neighbors()
        if n not in path and G.get(n, "#") != "#"
    ]
    assert neighbors or last == finish, path
    if len(neighbors) > 1 or last == finish:
        return path, dirs
    c = G[last]
    if c in DIRS:
        if DIRS[c] == (neighbors[0] - last):
            dirs = {1} & dirs
        else:
            assert DIRS[c] == (last - neighbors[0]), (path, neighbors[0])
            dirs = {-1} & dirs
    return path_to_next_node(path + [neighbors[0]], finish, dirs=dirs)


def build_graphs(start, finish):
    edges = {}
    directed_edges = {}
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
            path, dirs = path_to_next_node([node, n], finish)
            other = path[-1]
            length = len(path) - 1
            edges.setdefault(node, []).append((other, length))
            edges.setdefault(other, []).append((node, length))
            if 1 in dirs:
                directed_edges.setdefault(node, []).append((other, length))
            if -1 in dirs:
                directed_edges.setdefault(other, []).append((node, length))
            seen.update(path)
            to_process.append(other)
        processed.add(node)
    return edges, directed_edges


def dfs(E, start, finish, seen=None, cost=0):
    if start == finish:
        yield cost
    else:
        seen = (seen or set()) ^ {start}
        for n, stepcost in E[start]:
            if n in seen:
                continue
            yield from dfs(E, n, finish, seen=seen, cost=cost+stepcost)


U, D = build_graphs(START, FINISH)

print(max(dfs(D, START, FINISH)))
print(max(dfs(U, START, FINISH)))
