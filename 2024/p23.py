import sys

lines = [ln.strip().split("-") for ln in open(sys.argv[1])]

g = {}
for a, b in lines:
    a, b = sorted((a, b))
    g.setdefault(a, set()).add(b)


r = []
for s in g:
    for t in g[s]:
        for u in g.get(t, set()):
            if u not in g[s]:
                continue
            tup = [s, t, u]
            r.append(tup)


print(sum([any(m[0] == 't' for m in tup) for tup in r]))
