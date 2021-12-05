import sys
from collections import Counter
from itertools import cycle

lines = []
for ln in open(sys.argv[1]):
    start, finish = ln.split(" -> ")
    lines.append(
        (
            tuple(int(x) for x in start.split(",")),
            tuple(int(x) for x in finish.split(","))
        )
    )


def ranger(a, b):
    if a == b:
        return cycle([a])
    direction = 1 if a < b else -1
    return range(a, b + direction, direction)


straight_counts = Counter()
all_counts = Counter()
for start, finish in lines:
    straight = (start[0] == finish[0]) or (start[1] == finish[1])
    line_points = zip(ranger(start[0], finish[0]), ranger(start[1], finish[1]))
    for pt in line_points:
        all_counts[pt] += 1
        if straight:
            straight_counts[pt] += 1


# part 1: 7414
print(len([v for v in straight_counts.values() if v > 1]))

# part 2: 19676
print(len([v for v in all_counts.values() if v > 1]))
