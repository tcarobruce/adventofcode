import sys
import re
from collections import defaultdict


lines = [ln.strip() for ln in open(sys.argv[1])]
counts = [1] * len(lines)

p1_tot = 0
for i, ln in enumerate(lines):
    game, nums = ln.split(":")
    win, scratch = nums.split("|")
    win = [int(s) for s in re.findall("\d+", win)]
    scratch = [int(s) for s in re.findall("\d+", scratch)]
    matched = len(set(win) & set(scratch))
    if matched:
        p1_tot += 2**(matched - 1)
    current = counts[i]
    for j in range(i + 1, i + 1 + matched):
        counts[j] += current

print(p1_tot)
print(sum(counts))
