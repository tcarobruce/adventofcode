import sys
from collections import defaultdict

lines = open(sys.argv[1]).read().splitlines()

moments = set(range(20, 221, 40))


def process(lines):
    X = 1
    cycle = 1
    for line in lines:
        parts = line.split()
        if parts[0] == "noop":
            cycle += 1
            yield cycle, X
        elif parts[0] == "addx":
            cycle += 1
            yield cycle, X
            cycle += 1
            X += int(parts[1])
            yield cycle, X


tot = 0
print("#", end="")
for cycle, X in process(lines):
    if cycle in moments:
        tot += X * cycle
    if (cycle - 1) % 40 == 0:
        print()
    if abs(X - ((cycle - 1)% 40)) <= 1:
        print("#", end="")
    else:
        print(".", end="")

print()
print(tot)

