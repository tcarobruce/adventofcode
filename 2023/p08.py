import sys
import re
from itertools import cycle

lines = [ln.strip() for ln in open(sys.argv[1])]

turns = cycle(lines[0])

M = {}

for ln in lines[2:]:
    n, l, r = re.findall(r"[A-Z]{3}", ln)
    M[n] = (l, r)

node = "AAA"
count = 0

while node != "ZZZ":
    count += 1
    node = M[node][next(turns) == "R"]

print(count)


