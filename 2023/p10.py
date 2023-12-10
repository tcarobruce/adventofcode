import sys
from util import Vec
from collections import defaultdict


G = defaultdict(lambda: '.')
S = None
for y, line in enumerate(open(sys.argv[1])):
    for x, c in enumerate(line.strip()):
        if c == ".":
            continue
        elif c == "S":
            S = Vec(x, y)
        G[Vec(x, y)] = c


seen = {S}


def next_step(pos, last):
    c = G[pos]
    if c in "|-":
        return pos + (pos - last)
    if c == "L":
        if pos.els[0] == last.els[0]:
            return pos + Vec(1, 0)
        else:
            return pos - Vec(0, 1)
    elif c == "J":
        if pos.els[0] == last.els[0]:
            return pos - Vec(1, 0)
        else:
            return pos - Vec(0, 1)
    if c == "7":
        if pos.els[0] == last.els[0]:
            return pos - Vec(1, 0)
        else:
            return pos + Vec(0, 1)
    if c == "F":
        if pos.els[0] == last.els[0]:
            return pos + Vec(1, 0)
        else:
            return pos + Vec(0, 1)


def first_steps(s):
    if G[s + Vec(0, 1)] in "|JL":
        yield s + Vec(0, 1)
    if G[s + Vec(1, 0)] in "-J7":
        yield s + Vec(1, 0)
    if G[s + Vec(0, -1)] in "|7F":
        yield s + Vec(0, -1)
    if G[s + Vec(-1, 0)] in "-LF":
        yield s + Vec(-1, 0)


def follow(pos, last):
    while True:
        yield pos
        pos, last = next_step(pos, last), pos


start = list(first_steps(S))
assert len(start) == 2
apos, bpos = start
af = follow(apos, S)
bf = follow(bpos, S)
count = 0

seen = {S}

while True:
    count += 1
    apos = next(af)
    bpos = next(bf)
    print(apos, bpos)

    if apos == bpos:
        print(f"Same spot at {count}!")
        break
    elif apos in seen or bpos in seen:
        print(seen, apos, bpos)
        print(f"already seen at {count}!")
        break
    seen.add(apos)
    seen.add(bpos)


