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
    return sum([
        paths_to_end(edges, n, seen)
        for n in edges[node]
    ])


# part 1: 3576
print(paths_to_end(edges))


def paths_to_end_twosmalls(edges, node="start", seen=set(), seen_once=None):
    seen = seen.copy()
    if node == "end":
        return 1
    if node in seen and (seen_once or node in ("start", "end")):
        return 0
    elif node in seen:
        return sum([
            paths_to_end_twosmalls(edges, n, seen, seen_once=node)
            for n in edges[node]
        ])
    if not is_big(node):
        seen.add(node)
    return sum([
        paths_to_end_twosmalls(edges, n, seen, seen_once=seen_once)
        for n in edges[node]
    ])

print(paths_to_end_twosmalls(edges))
