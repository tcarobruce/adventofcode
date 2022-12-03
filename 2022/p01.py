import sys

groups = open(sys.argv[1]).read().split("\n\n")

calories = []
for group in groups:
    calories.append(
        sum(
            [
                int(ln.strip()) for ln in group.split("\n") if ln.strip()
            ]
        )
    )

calories.sort()
print(calories[-1])
print(sum(calories[-3:]))
