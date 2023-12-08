import sys
import re
from itertools import cycle
from math import prod
from util import lcm

lines = [ln.strip() for ln in open(sys.argv[1])]

turns = cycle(lines[0])

M = {}

for ln in lines[2:]:
    n, l, r = re.findall(r"[A-Z0-9]{3}", ln)
    M[n] = (l, r)

node = "AAA"
count = 0

while node != "ZZZ":
    count += 1
    node = M[node][next(turns) == "R"]

# p1
print(count)

# For part 2:
# Running through every step will take a long time.
# By observation, there are cycles, and they
# start at 0. (This happens to be true for this problem,
# but is not guaranteed.)

nodes = [n for n in M if n[-1] == "A"]

zhits = {}
intervals = {}
firsts = {}
count = 0
turns = cycle(lines[0])
while len(intervals) < len(nodes):
    for i, n in enumerate(nodes, 1):
        if n[-1] == "Z":
            k = (i, n)
            if k in zhits:
                interval = count - zhits[k]
                intervals.setdefault(i, set()).add(interval)
            if i not in firsts:
                firsts[i] = count
            zhits[k] = count

    count += 1
    turn = next(turns)
    nodes = [M[node][turn == "R"] for node in nodes]


print(intervals)
print(firsts)
print(lcm(*(next(iter(s)) for s in intervals.values())))
