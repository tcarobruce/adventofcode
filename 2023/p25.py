import sys
from random import choice
from copy import deepcopy
from math import prod

V = set()
E = []

lines = [ln.strip() for ln in open(sys.argv[1])]

for line in lines:
    s, ds = line.split(": ")
    V.add(s)
    for d in ds.split():
        V.add(d)
        E.append((s, d))


def contract(v, e):
    a, b = choice(list(e))
    # print("contracting", a, b)
    ab = '-'.join([a, b])
    v = (v - {a, b}) ^ {ab}

    ne = []
    for x, y in e:
        if {x, y} == {a, b}:
            continue
        elif x in {a, b}:
            ne.append((y, ab))
        elif y in {a, b}:
            ne.append((x, ab))
        else:
            ne.append((x, y))
    return v, ne


def mincut(v, e):
    while len(v) > 2:
        v, e = contract(v, e)
    return v, e


def find_mincut(v, e, n=3):
    while True:
        vp, ep = mincut(v, e)
        if len(ep) <= n:
            return vp, ep
        print(len(e))

v, e = find_mincut(V, E)

print(len(e), v)
print(prod([len(p.split("-")) for p in v]))
