import sys
from functools import cache

codes = [ln.strip() for ln in open(sys.argv[1])]

rows = "789 456 123 .0A".split()
npad = {
    k: (x, y) for y, row in enumerate(rows) for x, k in enumerate(row)
    if k != '.'
}
rows = ".^A <v>".split()
dpad = {
    k: (x, y) for y, row in enumerate(rows) for x, k in enumerate(row)
    if k != '.'
}

def x_legal(key, xoff, level):
    if xoff >= 0:
        return True
    if level == 0:
        return not (key == "0" or (key == "A" and xoff < -1))
    else:
        return not (key == "^" or (key == "A" and xoff < -1))


def sequence(code, pad, level=0):
    key = "A"
    moves = ""
    for next_key in code:
        xoff, yoff = [(t - f) for t, f in zip(pad[next_key], pad[key])]
        xs = abs(xoff) * ('<' if xoff < 0 else '>')
        ys = abs(yoff) * ('^' if yoff < 0 else 'v')
        if x_legal(key, xoff, level):
            moves += xs + ys
        else:
            moves += ys + xs
        moves += "A"
        key = next_key
    return moves


def getint(code):
    return int(code.lstrip("0").rstrip("A"))

tot = 0
for code in codes:
    d1 = sequence(code, npad)
    d2 = sequence(d1, dpad, 1)
    d3 = sequence(d2, dpad, 2)
    for c in [code, d1, d2, d3]:
        print(c, len(c))
    tot += len(d3) * getint(code)
    print()
print(tot)
