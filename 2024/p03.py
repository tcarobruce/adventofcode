import sys
import re

text = open(sys.argv[1]).read().strip()

tot = 0
for x, y in re.findall(r'mul\((\d+),(\d+)\)', text):
    tot += int(x) * int(y)
print(tot)

tot = 0
enabled = True
for m in re.finditer(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))", text):
    op = m.group(1)
    if op == 'do()':
        enabled = True
    elif op == "don't()":
        enabled = False
    elif enabled:
        tot += int(m.group(2)) * int(m.group(3))

print(tot)
