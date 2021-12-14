import sys
from collections import Counter

lines = [ln.strip() for ln in open(sys.argv[1])]

polymer = list(lines[0])

rules = dict(ln.split(' -> ') for ln in lines[2:])

def iter_polymer(s):
    out = []
    for a, c in zip(s, s[1:]):
        out.append(a)
        b = rules[a + c]
        out.append(b)
    out.append(c)
    return out

for _ in range(10):
    polymer = iter_polymer(polymer)

counts = Counter(polymer).most_common()
print(counts)
print(counts[0][1] - counts[-1][1])
