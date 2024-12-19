import sys
import re

f = open(sys.argv[1]).read()
patterns, towels = f.strip().split("\n\n")
patterns = patterns.split(", ")
towels = towels.split("\n")


patt = re.compile("^(" + "|".join(patterns) + ")*$")
print(len([t for t in towels if patt.match(t)]))
