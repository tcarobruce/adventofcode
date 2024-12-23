import sys

lines = [ln.strip().split("-") for ln in open(sys.argv[1])]

g = {}
for a, b in lines:
    a, b = sorted((a, b))
    g.setdefault(a, []).append(b)
    g.setdefault(b, []).append(a)


r = []
for s in g:
    for t in g[s]:
        if t <= s:
            continue
        for u in g[t]:
            if u <= t or u <= s or u not in g[s]:
                continue
            tup = [s, t, u]
            tup.sort()
            r.append(tup)


r.sort()
r = [tup for tup in r if any(m[0] == 't' for m in tup)]
for tup in r:
    print(tup)

print(len(r))
