import sys
import re
from util import Vec as V
from bisect import insort_left, bisect
from itertools import groupby
from collections import defaultdict

patt = re.compile(r"([RLDU]) (\d+) \(#([a-f0-9]{6})\)")
lines = [patt.match(ln.strip()).groups() for ln in open(sys.argv[1])]
dirs = [
    ("R", V(1, 0)),
    ("D", V(0, 1)),
    ("L", V(-1, 0)),
    ("U", V(0, -1)),
]
dirs_dict = dict(dirs)
dig_plan = [
    (dirs_dict[direction], int(count))
    for direction, count, _ in lines
]
dig_plan2 = [
    (dirs[int(color[-1])][1], int(color[:5], 16))
    for _, _, color in lines
]

def vertices(plan):
    pos = V(0, 0)
    for direction, count in plan:
        pos += direction * count
        yield pos, count


def shoelace(plan):
    last = start = V(0, 0)
    length = 0
    area = 0
    for pos, count in vertices(plan):
        area += (pos.els[1] + last.els[1]) * (last.els[0] - pos.els[0])
        length += count
        last = pos
    area += (start.els[1] + last.els[1]) * (last.els[0] - start.els[0])
    area += length + 2
    return area // 2

print(shoelace(dig_plan))
print(shoelace(dig_plan2))


def find_horizontal_segments(plan):
    segs = []
    pos = V(0, 0)
    lines = defaultdict(list)
    for direction, count in plan:
        if direction.els[0] == 0:
            lines[direction].append(count)
            pos += direction * count
        else:
            lines[direction].append(count)
            next_pos = pos + (direction * count)
            #r = direction == V(1, 0)
            insort_left(segs, (min(pos.els[0], next_pos.els[0]), pos.els[1], True))
            insort_left(segs, (max(pos.els[0], next_pos.els[0]), pos.els[1], False))
            pos = next_pos
    return segs, lines


def sum_segments(segments, lines):
    assert len(segments) % 2 == 0
    open_spans = []
    total = 0
    lastx = None
    for x, g in groupby(segments, lambda r: r[0]):
        for start, stop in zip(open_spans[::2], open_spans[1::2]):
            area = (x - lastx) * (stop - start)
            #print(lastx, x, start, stop, area)
            total += area
        for _, y, starting in g:
            if starting:
                insort_left(open_spans, y)
            else:
                i = bisect(open_spans, y)
                open_spans = open_spans[:i - 1] + open_spans[i:]
        lastx = x
    return total + sum(lines[V(1, 0)]) + sum(lines[V(0, 1)]) + 1

print(sum_segments(*find_horizontal_segments(dig_plan)))
print(sum_segments(*find_horizontal_segments(dig_plan2)))
