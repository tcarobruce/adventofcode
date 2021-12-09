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


def get_risk(heights):
    risk = 0
    for y, row in enumerate(heights):
        for x, height in enumerate(row):
            if all(
                height < heights[ny][nx]
                for nx, ny in neighbors(x, y)
            ):
                risk += height + 1
    return risk


print(get_risk(heights))
