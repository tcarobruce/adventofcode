import sys

groups = open(sys.argv[1]).read().split("\n\n")

calories = [0]
for ln in open(sys.argv[1]):
    ln = ln.strip()
    if not ln:
        calories.append(0)
        continue
    calories[-1] += int(ln)

calories.sort()
print(calories[-1])
print(sum(calories[-3:]))
