import sys
from util import readints

lines = [readints(ln) for ln in open(sys.argv[1])]
left, right = zip(*lines)
print(sum([abs(l - r) for l, r in zip(sorted(left), sorted(right))]))  # part 1
