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

def sequence(init_code, max_level):
    key = "A"
    result = ""
    q = [(init_code, 0, 0)]
    partner_1 = None
    while q:
        print(q)
        code, level, partner = q.pop()
        pad = dpad if level else npad
        code_results = []
        for next_key in code:
            xoff, yoff = [(t - f) for t, f in zip(pad[next_key], pad[key])]
            xs = abs(xoff) * ('<' if xoff < 0 else '>')
            ys = abs(yoff) * ('^' if yoff < 0 else 'v')
            if xoff and yoff and x_legal(key, xoff, level):
                moves = [xs + ys + "A", ys + xs + "A"]
            else:
                moves = [ys + xs + "A"]
            if level == max_level:
                if partner == 0:
                    m = moves[0]
                    if partner_1 and len(partner_1) < len(m):
                        m = partner_1
                    result += m
                    partner_1 = None
                elif partner == 1:
                    partner_1 = moves[0]
            else:
                for i, seq in enumerate(moves):
                    q.append((seq, level + 1, i))
            key = next_key
    return result


def getint(code):
    return int(code.lstrip("0").rstrip("A"))


print(sum([len(sequence(code, 2)) * getint(code) for code in codes]))
#print(sum([len(sequence(code, 5)) * getint(code) for code in codes]))
