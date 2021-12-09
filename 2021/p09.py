import sys
heights = []
for ln in open(sys.argv[1]):
    heights.append([int(c) for c in ln.strip()])

maxy = len(heights) - 1
maxx = len(heights[0]) - 1

def neighbors(x, y):
    if y > 0:
        yield (x, y - 1)
    if y < maxy:
        yield (x, y + 1)
    if x > 0:
        yield (x - 1, y)
    if x < maxx:
        yield (x + 1, y)


def find_low_points(heights):
    for y, row in enumerate(heights):
        for x, height in enumerate(row):
            if all(
                height < heights[ny][nx]
                for nx, ny in neighbors(x, y)
            ):
                yield x, y

def get_risk(heights):
    return sum([heights[y][x] + 1 for x, y in find_low_points(heights)])

# part 1: 537
print(get_risk(heights))

def find_basin_size(heights, lowx, lowy):
    q = [(lowx, lowy)]
    size = 0
    while q:
        x, y = q.pop(0)
        for nx, ny in neighbors(x, y):
            height = heights[ny][nx]
            if height is None or height == 9:
                continue
            q.append((nx, ny))
            heights[ny][nx] = None
            size += 1
    return size

def find_basin_sizes(heights):
    sizes = []
    low_points = list(find_low_points(heights))
    for x, y in low_points:
        sizes.append(find_basin_size(heights, x, y))
    return sizes

sizes = find_basin_sizes(heights)
sizes.sort()
print(sizes[-3] * sizes[-2] * sizes[-1])
# part 2: 1142757
