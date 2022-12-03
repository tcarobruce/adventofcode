import sys
from operator import and_
from functools import reduce
from string import ascii_letters

lines = [ln.strip() for ln in open(sys.argv[1])]

def priority(c):
    return ascii_letters.index(c) + 1

def intersect(*its):
    return reduce(and_, (set(it) for it in its))

def score_intersection(*its):
    return priority(intersect(*its).pop())

def bisect(ln):
    mid = len(ln) // 2
    return ln[:mid], ln[mid:]

# part 1
print(sum([score_intersection(*bisect(ln)) for ln in lines]))  # 7766

def triples(lines):
    it = iter(lines)
    return zip(it, it, it)

# part 2
print(sum([score_intersection(*trip) for trip in triples(lines)]))  # 2415
