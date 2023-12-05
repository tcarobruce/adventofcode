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

def overlap(a, b):
    return range(max(a.start, b.start), min(a.stop, b.stop))


def test_overlaps(ranges):
    for i, a in enumerate(ranges):
        for b in ranges[i + 1:]:
            if overlap(a, b):
                print(f"{a} overlaps with {b}")




maps = [read_map(chunk) for chunk in text[1:]]

for m in maps:
    test_overlaps([x[0] for x in m])


# p1
positions = seeds
for m in maps:
    positions = [find_destination(m, p) for p in positions]

print(min(positions))
