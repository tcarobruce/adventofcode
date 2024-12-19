import sys
import re
from functools import cache

f = open(sys.argv[1]).read()
patterns, towels = f.strip().split("\n\n")
patterns = patterns.split(", ")
towels = towels.split("\n")


patt = re.compile("^(" + "|".join(patterns) + ")*$")
print(len([t for t in towels if patt.match(t)]))

@cache
def ways(towel):
    if towel == "":
        return 1
    w = 0
    for pattern in patterns:
        if towel.startswith(pattern):
            w += ways(towel[len(pattern):])
    return w

print(sum([ways(t) for t in towels]))
