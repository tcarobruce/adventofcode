import sys
from collections import deque

grid = [[int(c) for c in ln.strip()] for ln in open(sys.argv[1])]


def neighbors(x, y):
    for ny in range(max(y - 1, 0), min(y + 2, 10)):
        for nx in range(max(x - 1, 0), min(x + 2, 10)):
            if x == nx and y == ny:
                continue
            yield nx, ny


def itergrid(grid):
    flashes = 0
    flashy = deque()
    flashed = set()
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            row[x] += 1
            if row[x] > 9:
                flashy.append((x, y))
    while flashy:
        t = flashy.popleft()
        if t in flashed:
            continue
        flashed.add(t)
        x, y = t
        for nx, ny in neighbors(x, y):
            if (nx, ny) in flashed:
                continue
            grid[ny][nx] += 1
            if grid[ny][nx] > 9:
                flashy.append((nx, ny))
        grid[y][x] = 0
        flashes += 1
    return flashes


def print_grid(grid):
    print()
    for row in grid:
        print("".join([str(n) for n in row]))


total_flashes = 0
for step in range(101):
    print()
    print(f"After step {step}:")
    print_grid(grid)
    print(total_flashes)
    total_flashes += itergrid(grid)

# part 1: 1627


