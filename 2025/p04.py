import sys

from util import readgridv


G = {g for g, v in readgridv(open(sys.argv[1])).items() if v == "@"}
candidates = set(G)
p1_done = False
total = 0

while True:
    to_remove = set()
    next_candidates = set()
    for g in candidates:
        nabes = {n for n in g.neighbors_diag() if n in G}
        if len(nabes) < 4:
            to_remove.add(g)
            next_candidates |= nabes

    total += len(to_remove)

    if not p1_done:
        print(total)
        p1_done = True

    if not to_remove:
        print(total)
        break

    G = G - to_remove
    candidates = next_candidates & G
