import sys
import re


def get_ints(s):
    return [int(m) for m in re.findall(r"\d+", s)]


text = open(sys.argv[1]).read().split("\n\n")

positions = get_ints(text[0])


def read_map(chunk):
    lines = chunk.strip().split("\n")
    print(f"handling {lines[0]}")
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



for chunk in text[1:]:
    m = read_map(chunk)
    positions = [find_destination(m, p) for p in positions]

print(min(positions))


