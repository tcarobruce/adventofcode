import sys

groups = open("p01_input.txt").read().split("\n\n")

m = 0
for group in groups:
    calories = sum(
        [
            int(ln.strip()) for ln in group.split("\n") if ln.strip()
        ]
    )
    m = max(calories, m)

print(m)
