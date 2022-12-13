import sys
from itertools import zip_longest
from functools import cmp_to_key

FILL = object()

doc = open(sys.argv[1]).read()
pairs = [[eval(ln) for ln in p.strip().split("\n")] for p in doc.split("\n\n")]

def cmp(a, b):
    return (a > b) - (a < b)

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return cmp(a, b)
    if isinstance(a, list) and isinstance(b, list):
        for ai, bi in zip_longest(a, b, fillvalue=FILL):
            if ai == FILL:
                return -1
            elif bi == FILL:
                return 1
            r = compare(ai, bi)
            if r != 0:
                return r
        return 0
    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    if isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    assert False, "bad juju %r %r" % (a, b)


total = 0
for i, (a, b) in enumerate(pairs, 1):
    if compare(a, b) < 0:
        total += i
print(total)

distress = [[[2]], [[6]]]
all_lines = sum(pairs, distress)
all_lines.sort(key=cmp_to_key(compare))

result = 1
for i, ln in enumerate(all_lines, 1):
    if ln in distress:
        result *= i
print(result)
