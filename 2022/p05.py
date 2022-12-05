import sys
import re
from copy import deepcopy

stack_input, move_input = open(sys.argv[1]).read().split("\n\n")
crates = [ln[1::4] for ln in stack_input.splitlines()[:-1]]
stacks = [[c for c in t[::-1] if c != " "] for t in zip(*crates)]
stacks2 = deepcopy(stacks)

patt = re.compile(r'move (\d+) from (\d+) to (\d+)')

for line in move_input.splitlines():
    m = patt.match(line)
    count, src, dest = [int(x) for x in m.groups()]
    src -= 1
    dest -= 1
    for _ in range(count):
        stacks[dest].append(stacks[src].pop())
    stacks2[dest] += stacks2[src][-count:]
    stacks2[src] = stacks2[src][:-count]

for ss in [stacks, stacks2]:
    print("".join([s[-1] for s in ss]))
