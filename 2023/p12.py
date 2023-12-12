import sys

from util import *

lines = [ln.strip().split() for ln in open(sys.argv[1])]
lines = [(ln[0], readints(ln[1])) for ln in lines]


def try_chomp(s, pattern):
    amt = pattern[0]
    next_bit = s[:amt]
    if len(next_bit) == amt and set(next_bit) <= {"#", "?"} and (len(s) == amt or s[amt] in '.?'):
        return ways(s[amt + 1:], pattern[1:])
    else:
        return 0


def ways(s, pattern):
    if not pattern:
        return 1
    elif not s:
        return 0
    c = s[0]
    if c == '.':
        return ways(s[1:], pattern)
    if c == "#":
        return try_chomp(s, pattern)
    if c == "?":
        return ways(s[1:], pattern) + try_chomp(s, pattern)
    assert False, f"oops '{c}'"


tot = 0
for s, pattern in lines:
    w = ways(s, pattern)
    tot += w
    print(s, pattern, w)

print(tot)
