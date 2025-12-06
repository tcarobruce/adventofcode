import sys
import re
from math import prod

lines = open(sys.argv[1]).read().strip().split("\n")

# p1
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

total = 0
i = 0
numbers = lines[:-1]
ops = lines[-1]
maxx = len(lines[0])
problem_numbers = []
op = None

while i < maxx:
    if op is None:
        op = ops[i]
    n = 0
    for line in numbers:
        c = line[i]
        if c == " ":
            continue
        n = 10 * n + int(c)

    if n == 0:
        print(op, problem_numbers)
        if op == "+":
            total += sum(problem_numbers)
        elif op == "*":
            total += prod(problem_numbers)
        else:
            assert 0, f"op is {op}"
        op = None
        problem_numbers = []
    else:
        problem_numbers.append(n)

    i += 1

if op == "+":
    total += sum(problem_numbers)
elif op == "*":
    total += prod(problem_numbers)
else:
    assert 0, f"op is {op}"
print(total)
