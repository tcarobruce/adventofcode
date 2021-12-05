import sys
from collections import Counter

lines = []
for ln in open(sys.argv[1]):
    start, finish = ln.split(" -> ")
    lines.append(
        (
            tuple(int(x) for x in start.split(",")),
            tuple(int(x) for x in finish.split(","))
        )
    )

def line_points(start, finish):
    sx, fx = sorted([start[0], finish[0]])
    sy, fy = sorted([start[1], finish[1]])

    for x in range(sx, fx + 1):
        for y in range(sy, fy + 1):
            yield x, y

# part 1: 7414
counts = Counter()
for start, finish in lines:
    if (start[0] == finish[0]) or (start[1] == finish[1]):
        for pt in line_points(start, finish):
            counts[pt] += 1

print(len([v for v in counts.values() if v > 1]))
