import sys

from util import readgridv


G = readgridv(open(sys.argv[1]))
maxx = max([v.els[0] for v in G])
maxy = max([v.els[1] for v in G])

p1_done = False
total = 0

while True:
    to_remove = set()
    for g, val in G.items():
        if val != "@":
            continue
        nabes = sum([G.get(n, "") == "@" for n in g.neighbors_diag()])
        if nabes < 4:
            to_remove.add(g)

    total += len(to_remove)

    if not p1_done:
        print(total)
        p1_done = True

    if not to_remove:
        print(total)
        break

    for g in to_remove:
        G[g] = "."

