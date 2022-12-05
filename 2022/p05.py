import sys
import re
from copy import deepcopy

f = open(sys.argv[1])

stack_input, move_input = f.read().split("\n\n")
crates = [ln[1::4] for ln in stack_input.splitlines()[:-1]]
stacks = [[c for c in t[::-1] if c != " "] for t in zip(*crates)]

patt = re.compile(r'move (\d+) from (\d+) to (\d+)')
moves = []

for line in move_input.splitlines():
    m = patt.match(line)
    count, src, dest = [int(x) for x in m.groups()]
    moves.append((src - 1, dest - 1, count))  # zero-index

orig = stacks

# part 1
stacks = deepcopy(orig)
for src, dest, count in moves:
    for _ in range(count):
        stacks[dest].append(stacks[src].pop())
print("".join([s[-1] for s in stacks]))

# part 2
stacks = deepcopy(orig)
for src, dest, count in moves:
    stacks[dest] += stacks[src][-count:]
    stacks[src] = stacks[src][:-count]
print("".join([s[-1] for s in stacks]))
