import sys
from util import readints
lines = [readints(ln) for ln in open(sys.argv[1])]

def concat(a, b):
    return int(str(a) + str(b))

def test_line(line):
    goal = line[0]
    p1 = p2 = [line[1]]
    for o in line[2:]:
        p1 = [v + o for v in p1] + [v * o for v in p1]
        p2 = [v + o for v in p2] + [v * o for v in p2] + [concat(v, o) for v in p2]
    return (goal * (goal in p1), goal * (goal in p2))

tests = [test_line(ln) for ln in lines]
for p in zip(*tests):
    print(sum(p))
