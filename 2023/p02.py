import sys
import re
from math import prod

possible_maxs = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

lines = [ln.strip() for ln in open(sys.argv[1])]

linepatt = re.compile(r"Game (\d+)")
colorpatt = re.compile(r"([\d]+) (red|green|blue)")

p1_tot = 0
p2_tot = 0
for ln in lines:
    game = int(linepatt.match(ln).group(1))
    possible = True
    maxs = {"red": 0, "green": 0, "blue": 0}
    for amount, color in colorpatt.findall(ln):
        amount = int(amount)
        if amount > possible_maxs[color]:
            possible = False
        maxs[color] = max(maxs[color], amount)

    power = prod(maxs.values())
    p2_tot += power

    if possible:
        p1_tot += game

print(p1_tot)
print(p2_tot)
