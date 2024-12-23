import sys

lines = [ln.strip().split("-") for ln in open(sys.argv[1])]

g = {}
tups = []
for a, b in lines:
    a, b = sorted((a, b))
    tups.append((a, b))
    g.setdefault(a, set()).add(b)


def augment(tups):
    result = []
    for tup in tups:
        candidates = g.get(tup[0], set()) - set(tup)
        for c in candidates:
            if all(c in g.get(t, []) for t in tup):
                result.append(tup + (c,))
    return result


last = tups
while tups:
    print(len(tups[0]), len(tups))
    if len(tups[0]) == 3:
        print(sum([any(m[0] == 't' for m in tup) for tup in tups]))
    tups, last = augment(tups), tups

print(last)
print(",".join(sorted(last[0])))
