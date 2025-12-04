import sys

from util import readgridv


G = readgridv(open(sys.argv[1]))
maxx = max([v.els[0] for v in G])
maxy = max([v.els[1] for v in G])

print(G, maxx, maxy)

count = 0

for g, val in G.items():
    if val != "@":
        continue
    nabes = sum([G.get(n, "") == "@" for n in g.neighbors_diag()])
    if nabes < 4:
        print(g)
        count += 1

print(count)
