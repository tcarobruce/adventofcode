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

# part 1
print(len(visible))

def scenic_score(i, j):
    total = 1
    height = grid[i][j]
    score = 0
    for l in range(i - 1, -1, -1):
        score += 1
        if grid[l][j] >= height:
            break
    total *= score

    score = 0
    for l in range(i + 1, len(grid)):
        score += 1
        if grid[l][j] >= height:
            break
    total *= score

    score = 0
    for l in range(j - 1, -1, -1):
        score += 1
        if grid[i][l] >= height:
            break
    total *= score

    score = 0
    for l in range(j + 1, len(grid[0])):
        score += 1
        if grid[i][l] >= height:
            break
    total *= score

    return total

print(max([scenic_score(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]))
