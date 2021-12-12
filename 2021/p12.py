import sys
from collections import defaultdict
from string import ascii_uppercase

upcase = set(ascii_uppercase)


def is_big(s):
    return set(s) < upcase


edges = defaultdict(list)

for ln in open(sys.argv[1]):
    a, b = ln.strip().split("-")
    edges[a].append(b)
    edges[b].append(a)


def paths_to_end(edges, node="start", seen=set()):
    seen = seen.copy()
    if node in seen:
        return 0
    elif node == "end":
        return 1
    if not is_big(node):
        seen.add(node)
    r = sum([
        paths_to_end(edges, n, seen)
        for n in edges[node]
    ])
    return r


print(paths_to_end(edges))
