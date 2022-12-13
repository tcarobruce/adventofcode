import sys
from itertools import zip_longest
from functools import cmp_to_key
from math import prod

FILL = object()

doc = open(sys.argv[1]).read()
pairs = [
    [eval(ln) for ln in p.strip().split("\n")]
    for p in doc.split("\n\n")
]

def cmp(a, b):
    return (a > b) - (a < b)

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return cmp(a, b)
    elif isinstance(a, list) and isinstance(b, list):
        for ai, bi in zip_longest(a, b, fillvalue=FILL):
            if ai == FILL:
                return -1
            elif bi == FILL:
                return 1
            elif r := compare(ai, bi):
                return r
        return 0
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    assert False, "bad juju %r %r" % (a, b)


print(sum([i for i, (a, b) in enumerate(pairs, 1) if compare(a, b) < 0]))

distress = [[[2]], [[6]]]
all_lines = sum(pairs, distress)
all_lines.sort(key=cmp_to_key(compare))
print(prod([1 + all_lines.index(d) for d in distress]))
