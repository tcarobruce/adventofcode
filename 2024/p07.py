import sys
from util import readints
lines = [readints(ln) for ln in open(sys.argv[1])]

def test_line(line):
    goal = line[0]
    vals = [line[1]]
    for o in line[2:]:
        vals = [v + o for v in vals] + [v * o for v in vals]
    return goal in vals

def test_line2(line):
    goal = line[0]
    vals = [line[1]]
    for o in line[2:]:
        vals = [v + o for v in vals] + [v * o for v in vals] + [concat(v, o) for v in vals]
    return goal in vals


def concat(a, b):
    return int(str(a) + str(b))

tot = 0
tot2 = 0
for ln in lines:
    t = test_line2(ln)
    print(ln, t)
    if t:
        tot += ln[0]
print(tot)
