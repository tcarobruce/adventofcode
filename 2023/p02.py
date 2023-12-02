import sys
import re

maxs = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

lines = [ln.strip() for ln in open(sys.argv[1])]

linepatt = re.compile(r"Game (\d+)")
colorpatt = re.compile(r"([\d]+) (red|green|blue)")

tot = 0
for ln in lines:
    game = int(linepatt.match(ln).group(1))
    for amount, color in colorpatt.findall(ln):
        if int(amount) > maxs[color]:
            break
    else:
        tot += game

print(tot)
