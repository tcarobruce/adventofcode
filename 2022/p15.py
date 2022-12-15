import sys
import re

lines = open(sys.argv[1]).read().splitlines()
row = int(sys.argv[2])

sensors = []

p = re.compile(r"Sensor at x=([\d-]+), y=([\d-]+): closest beacon is at x=([\d-]+), y=([\d-]+)")

for line in lines:
    m = p.match(line)
    sensors.append([int(s) for s in m.groups()])

def dist(sensor):
    sx, sy, bx, by = sensor
    return abs(sx - bx) + abs(sy - by)

def range_for_row(sensor, row):
    sx, sy, bx, by = sensor
    d = dist(sensor)
    ydist = abs(sy - row)
    if ydist > d:
        return None
    xrad = d - ydist
    return range(sx - xrad, sx + xrad + 1)


def overlap(r1, r2):
    return max(r1[0], r2[0]) < min(r1.stop, r2.stop)

def add_ranges(r1, r2):
    # assumed overlapping
    return range(min(r1.start, r2.start), max(r1.stop, r2.stop))


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
    next_ranges.append(rr)
    ranges = next_ranges


print(sum([len(r) - 1 for r in ranges]))
