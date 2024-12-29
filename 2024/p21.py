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

def x_can_go_first(key, xoff, level):
    if xoff >= 0:
        return True
    if level == 0:
        return not (key == "0" or (key == "A" and xoff < -1))
    else:
        return not (key == "^" or (key == "A" and xoff < -1))

def y_can_go_first(key, yoff, level):
    if level == 0:
        return key not in "147" or "147".find(key) - yoff >= 0
    else:
        return key != "<" or yoff >= 0

@cache
def sequence(code, max_level, level=0):
    key = "A"
    result = 0
    pad = dpad if level else npad
    for next_key in code:
        xoff, yoff = [(t - f) for t, f in zip(pad[next_key], pad[key])]
        xs = abs(xoff) * ('<' if xoff < 0 else '>')
        ys = abs(yoff) * ('^' if yoff < 0 else 'v')
        if not xoff and not yoff:
            moves = ["A"]
        elif not xoff:
            moves = [ys + "A"]
        elif not yoff:
            moves = [xs + "A"]
        elif not x_can_go_first(key, xoff, level):
            moves = [ys + xs + "A"]
        elif not y_can_go_first(key, yoff, level):
            moves = [xs + ys + "A"]
        else:
            moves = [xs + ys + "A", ys + xs + "A"]
        if level == max_level:
            result += len(moves[0])
        else:
            result += min([sequence(seq, max_level, level=level+1) for seq in moves])
        key = next_key
    return result



def getint(code):
    return int(code.lstrip("0").rstrip("A"))


print(sum([sequence(code, 2) * getint(code) for code in codes]))
print(sum([sequence(code, 25) * getint(code) for code in codes]))
