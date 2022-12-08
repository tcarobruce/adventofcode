import sys

grid = [
    [int(c) for c in ln]
    for ln in open(sys.argv[1]).read().splitlines()
]

visible = set()

for i, row in enumerate(grid):
    left = right = -1
    l = len(row) - 1
    for j, height in enumerate(row):
        if height > left:
            visible.add((i, j))
            left = height

        height = row[l - j]
        if height > right:
            visible.add((i, l - j))
            right = height

for j in range(len(grid[0])):
    top = bottom = -1
    l = len(grid) - 1
    for i in range(len(grid)):
        height = grid[i][j]
        if height > top:
            visible.add((i, j))
            top = height

        height = grid[l - i][j]
        if height > bottom:
            visible.add((l - i, j))
            bottom = height

print(len(visible))
