import sys
from util import *

fn = sys.argv[1]
lines = [ln.strip() for ln in open(fn)]


def rotate_cw(lines):
    return [
        "".join([ln[i] for ln in lines][::-1])
        for i, _ in enumerate(lines[0])
    ]


def tilt_right(row):
    rounds = 0
    tilted = []
    for i, c in enumerate(row):
        if c == "O":
            rounds += 1
            c = "."
        elif c == "#":
            for j in range(rounds):
                tilted[i - j - 1] = "O"
            rounds = 0
        tilted.append(c)
    for j in range(rounds):
        tilted[len(tilted) - j - 1] = "O"
    return "".join(tilted)


def load(line):
    return sum([i for i, c in enumerate(line, 1) if c == "O"])


# p1
print(sum([load(tilt_right(ln)) for ln in rotate_cw(lines)]))


def cycle(lines):
    for _ in range(4):
        lines = [tilt_right(ln) for ln in rotate_cw(lines)]
    return lines


seen = {}
cycles = 1000000000
for i in range(cycles):
    k = "\n".join(lines)
    if k in seen:
        interval = i - seen[k]
        print(f"repeat at {i}, prev {seen[k]}, interval {i - seen[k]}")
        break
    seen[k] = i
    lines = cycle(lines)

mod = (cycles - i) % interval

for _ in range(mod):
    lines = cycle(lines)

print(sum([load(ln) for ln in rotate_cw(lines)]))
