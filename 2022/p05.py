import sys
import re

f = iter(open(sys.argv[1]))
stack_count = int(sys.argv[2])

stacks = [[] for _ in range(stack_count)]



for line in f:
    if line[1] == "1":
        next(f)
        break
    for s in range(stack_count):
        c = line[s * 4 + 1]
        if c != ' ':
            stacks[s].insert(0, c)

patt = re.compile(r'move (\d+) from (\d+) to (\d+)')

part1 = False
for line in f:
    m = patt.match(line)
    count, src, dest = [int(x) for x in m.groups()]
    src -= 1
    dest -= 1
    if part1:
        for _ in range(count):
            stacks[dest].append(stacks[src].pop())
    else:
        stacks[dest] += stacks[src][-count:]
        stacks[src] = stacks[src][:-count]

print(stacks)
print("".join([s[-1] for s in stacks]))
