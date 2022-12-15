import sys
import re
from operator import itemgetter

lines = open(sys.argv[1]).read().splitlines()
row = int(sys.argv[2])

sensors = []

p = re.compile(r"Sensor at x=([\d-]+), y=([\d-]+): closest beacon is at x=([\d-]+), y=([\d-]+)")

for line in lines:
    m = p.match(line)
    sx, sy, bx, by = [int(s) for s in m.groups()]
    dist = abs(sx - bx) + abs(sy - by)
    sensors.append((sx, sy, dist))


sensors.sort(key=itemgetter(1))  # help to sort by y?


def range_for_row(sensor, row):
    sx, sy, dist = sensor
    ydist = abs(sy - row)
    if ydist > dist:
        return None
    xrad = dist - ydist
    return (sx - xrad, sx + xrad + 1)


def overlap(r1, r2):
    return max(r1[0], r2[0]) < min(r1[-1], r2[-1])

def add_ranges(r1, r2):
    # assumed overlapping
    return (min(r1[0], r2[0]), max(r1[-1], r2[-1]))


def contains(r1, r2):
    return r1[0] <= r2[0] and r1[-1] >= r2[-1]


def find_ranges(row, lim=None):
    ranges = []
    for sensor in sensors:
        next_ranges = []
        rr = range_for_row(sensor, row)
        if rr is None:
            continue
        for ro in ranges:
            if overlap(rr, ro):
                rr = add_ranges(rr, ro)
            else:
                next_ranges.append(ro)
        if lim is not None and contains(rr, lim):
            return [rr]
        next_ranges.append(rr)
        ranges = next_ranges
    return ranges


print(sum([(r[-1] - r[0]) - 1 for r in find_ranges(row)]))

for row in range(0, 4000001):
    fr = find_ranges(row, lim=range(0, 4000001))
    if len(fr) > 1:
        print(row, fr)
        break
    if row % 100000 == 0:
        print(row)

print(4000000 * fr[0][-1] + row)
