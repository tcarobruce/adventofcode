import sys
import re


def get_ints(s):
    return [int(m) for m in re.findall(r"\d+", s)]


text = open(sys.argv[1]).read().split("\n\n")

seeds = get_ints(text[0])


def read_map(chunk):
    lines = chunk.strip().split("\n")
    maps = [get_ints(line) for line in lines[1:]]
    return [
        (range(source, source + length), destination - source)
        for destination, source, length in maps
    ]

def find_destination(m, source):
    for source_range, offset in m:
        if source in source_range:
            return source + offset
    else:
        return source

def range_overlap(a, b):
    return range(max(a.start, b.start), min(a.stop, b.stop))


def test_overlaps(ranges):
    for i, a in enumerate(ranges):
        for b in ranges[i + 1:]:
            if range_overlap(a, b):
                print(f"{a} overlaps with {b}")


def partition_range(a, b):
    # generate the intersection and difference of ranges a-b
    overlap = range(max(a.start, b.start), min(a.stop, b.stop))
    if overlap:
        left = range(a.start, overlap.start)
        right = range(overlap.stop, a.stop)
        disj = [x for x in [left, right] if x]
    else:
        disj = [a]
    return overlap, disj


def map_ranges(m, in_ranges):
    "map source ranges to destination ranges"
    out_ranges = []
    for source_range, offset in m:
        new_in_ranges = []
        for in_range in in_ranges:
            overlap, disj = partition_range(in_range, source_range)
            if overlap:
                # offset range to destination
                out_ranges.append(range(overlap.start + offset, overlap.stop + offset))
            new_in_ranges.extend(disj)
        in_ranges = new_in_ranges
    return out_ranges + in_ranges


maps = [read_map(chunk) for chunk in text[1:]]

# for m in maps:
#     test_overlaps([x[0] for x in m])


# p1
positions = seeds
for m in maps:
    positions = [find_destination(m, p) for p in positions]

print(min(positions))

# p2
ranges = [range(a, a + b) for a, b in zip(seeds[::2], seeds[1::2])]

for m in maps:
    ranges = map_ranges(m, ranges)

print(min([r.start for r in ranges]))
