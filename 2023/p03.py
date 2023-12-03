import sys
import re

lines = [ln.strip() for ln in open(sys.argv[1])]

total = 0

def neighbors_symbol(y, xstart, xstop):
    for line in lines[max(0, y-1):y+2]:
        if re.search(r"[^0-9\.]", line[max(0, xstart - 1):xstop + 1]):
            return True
    return False

for y, line in enumerate(lines):
    for m in re.finditer(r"\d+", line):
        if neighbors_symbol(y, m.start(), m.end()):
            total += int(m.group(0))

print(total)
