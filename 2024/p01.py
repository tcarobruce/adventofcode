import sys
from collections import Counter
from util import readints

lines = [readints(ln) for ln in open(sys.argv[1])]
left, right = zip(*lines)

print(sum([abs(l - r) for l, r in zip(sorted(left), sorted(right))]))  # part 1

count_right = Counter(right)
print(sum([l * count_right[l] for l in left]))  # part 2
