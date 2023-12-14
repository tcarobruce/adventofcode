import sys
from util import *

fn = sys.argv[1]
lines = [ln.strip() for ln in open(fn)]


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


tot = 0
for i, _ in enumerate(lines[0]):
    ln = tilt_right([ln[i] for ln in lines][::-1])
    print(ln, load(ln))
    tot += load(ln)

print(tot)
