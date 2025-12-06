import sys
import re
from math import prod

lines = open(sys.argv[1]).read().strip().split("\n")

numbers = [[int(s) for s in ln.strip().split()] for ln in lines[:-1]]
ops = lines[-1].split()
assert len({len(s) for s in numbers + [ops]}) == 1

total = 0
for i, op in enumerate(ops):
    if op == "+":
        total += sum([ns[i] for ns in numbers])
    elif op == "*":
        total += prod([ns[i] for ns in numbers])

print(total)


