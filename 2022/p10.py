import sys

lines = open(sys.argv[1]).read().splitlines()


def process(lines):
    X = 1
    for line in lines:
        parts = line.split()
        if parts[0] == "noop":
            yield X
        elif parts[0] == "addx":
            yield X
            yield X
            X += int(parts[1])

tot = 0
moments = set(range(20, 221, 40))

for cycle, X in enumerate(process(lines), 1):
    # part 1
    if (cycle + 20) % 40 == 0:
        tot += X * cycle

    # part 2
    c, end = ".", ""
    if abs(X - ((cycle - 1) % 40)) <= 1:
        c = "#"
    if (cycle) % 40 == 0:
        end = "\n"
    print(c, end=end)

print()
print(tot)

