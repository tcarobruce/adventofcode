import sys
from util import readints

lines = [tuple(readints(ln)) for ln in open(sys.argv[1])]
left, right = zip(*lines)
left = list(left)
right = list(right)
left.sort()
right.sort()
print(sum([abs(l - r) for l, r in zip(left, right)]))
