import sys
import re
from copy import deepcopy

f = iter(open(sys.argv[1]))

stacks = None
stack_count = None

for line in f:
    if stacks is None:
        stack_count = len(line) // 4
        stacks = [[] for _ in range(stack_count)]
    if "[" not in line:
        next(f)  # skip blank line
        break
    stack = 0
    for stack in range(stack_count):
        c = line[stack * 4 + 1]
        if c != " ":
            stacks[stack].insert(0, c)

patt = re.compile(r'move (\d+) from (\d+) to (\d+)')
moves = []

for line in f:
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
