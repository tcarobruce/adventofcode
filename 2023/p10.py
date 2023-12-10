import sys
from util import Vec
from collections import defaultdict


G = defaultdict(lambda: '.')
S = None
lines = [ln.strip() for ln in open(sys.argv[1])]
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "S":
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

loop = {S}

while True:
    count += 1
    apos = next(af)
    bpos = next(bf)

    if apos == bpos:
        print(f"Same spot at {count}!")
        loop.add(apos)
        break
    elif apos in loop or bpos in loop:
        print(f"already seen at {count}!")
        loop.add(apos)
        loop.add(bpos)
        break
    loop.add(apos)
    loop.add(bpos)

enclosed = 0
for y, line in enumerate(lines):
    inloop = False
    bias = None
    #print(y, line)
    for x, c in enumerate(line):
        if c == "S":
            c = sys.argv[2]
        if Vec(x, y) in loop:
            if c == "|":
                inloop = not inloop
            elif c == "L":
                assert not bias
                bias = "J"
            elif c == "F":
                assert not bias
                bias = "7"
            elif c == "J":
                assert bias
                if c != bias:
                    inloop = not inloop
                bias = None
            elif c == "7":
                assert bias
                if c != bias:
                    inloop = not inloop
                bias = None
        elif inloop:
            enclosed += 1
            #print((x, y), G[Vec(x, y)])

print(enclosed)
