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


def paths_to_end(edges, node="start", seen=set(), allow_repeat=False):
    if node == "end":
        return 1
    if node in seen and (not allow_repeat or node == "start"):
        return 0
    elif node in seen:
        allow_repeat = False
    if not is_big(node):
        seen = seen | {node}
    return sum([
        paths_to_end(edges, n, seen, allow_repeat=allow_repeat)
        for n in edges[node]
    ])


# part 1: 3576
print(paths_to_end(edges))
# part 2: 84271
print(paths_to_end(edges, allow_repeat=True))
