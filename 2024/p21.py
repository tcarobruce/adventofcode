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

@cache
def sequence(code, max_level, level=0):
    key = "A"
    result = ""
    pad = dpad if level else npad
    print(level)
    for next_key in code:
        xoff, yoff = [(t - f) for t, f in zip(pad[next_key], pad[key])]
        xs = abs(xoff) * ('<' if xoff < 0 else '>')
        ys = abs(yoff) * ('^' if yoff < 0 else 'v')
        if xoff and yoff and x_legal(key, xoff, level):
            moves = [xs + ys + "A", ys + xs + "A"]
        else:
            moves = [ys + xs + "A"]
        if level == max_level:
            result += moves[0]
        else:
            m = min([sequence(seq, max_level, level=level+1) for seq in moves], key=lambda s: len(s))
            # if level == 1 and xoff and yoff and x_legal(key, xoff, level) and m != xs + ys + 'A':
            #     print("DEVIANT", level, key, next_key, xoff, yoff, m)
            result += m
        key = next_key
    return result


def getint(code):
    return int(code.lstrip("0").rstrip("A"))


print(sum([len(sequence(code, 2)) * getint(code) for code in codes]))
print(sum([len(sequence(code, 25)) * getint(code) for code in codes]))
