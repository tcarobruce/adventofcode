import sys
from collections import Counter
from itertools import zip_longest

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
    r = range(min(a, b), max(a, b) + 1)
    if a > b:
        r = reversed(r)
    return r

def line_points(start, finish):
    fillvalue = None
    xs, ys = (), ()
    if start[0] == finish[0]:
        fillvalue = start[0]
    else:
        xs = ranger(start[0], finish[0])
    if start[1] == finish[1]:
        fillvalue = start[1]
    else:
        ys = ranger(start[1], finish[1])
    return zip_longest(xs, ys, fillvalue=fillvalue)


straight_counts = Counter()
all_counts = Counter()
for start, finish in lines:
    straight = (start[0] == finish[0]) or (start[1] == finish[1])
    for pt in line_points(start, finish):
        all_counts[pt] += 1
        if straight:
            straight_counts[pt] += 1

# part 1: 7414
print(len([v for v in straight_counts.values() if v > 1]))

# part 2
print(len([v for v in all_counts.values() if v > 1]))
