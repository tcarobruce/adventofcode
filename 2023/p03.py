import sys
import re
import math
from collections import defaultdict

lines = [ln.strip() for ln in open(sys.argv[1])]

total = 0

def find_symbols(y, xstart, xstop):
    any_symbol = False
    gears = []
    for yoff in [-1, 0, 1]:
        yline = y + yoff
        if yline < 0:
            continue
        if yline >= len(lines):
            break
        line = lines[yline]
        xoff = max(0, xstart - 1)
        if re.search(r"[^0-9\.]", line[xoff:xstop + 1]):
            any_symbol = True
        for m in re.finditer(r"\*", line[xoff:xstop + 1]):
            gears.append((xoff + m.start(), yline))
    return any_symbol, gears


GEARS = defaultdict(list)

for y, line in enumerate(lines):
    for m in re.finditer(r"\d+", line):
        num = int(m.group(0))
        any_symbol, gears = find_symbols(y, m.start(), m.end())
        if any_symbol:
            total += num

        for g in gears:
            GEARS[g].append(num)

print(total)
print(sum([math.prod(gears) for gears in GEARS.values() if len(gears) == 2]))
