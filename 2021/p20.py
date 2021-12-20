import sys

lines = (ln.strip() for ln in open(sys.argv[1]))

iea_string = next(lines)
next(lines)

image = set()
for y, ln in enumerate(lines):
    for x, c in enumerate(ln):
        if c == '#':
            image.add((x, y))


def neighbors(x, y):
    for j in range(-1, 2):
        for i in range(-1, 2):
            yield x + i, y + j


def enhance_pixel(x, y, image):
    n = 0
    for xx, yy in neighbors(x, y):
        if (xx, yy) in image:
            n += 1
        n <<= 1
    return iea_string[n>>1] == "#"


def image_bounds(image):
    pts = iter(image)
    x, y = next(pts)
    xmin = xmax = x
    ymin = ymax = y
    for x, y in pts:
        xmin = min(x, xmin)
        xmax = max(x, xmax)
        ymin = min(y, ymin)
        ymax = max(y, ymax)
    return (xmin, xmax, ymin, ymax)


def render(image):
    pixels = ".#"
    xmin, xmax, ymin, ymax = image_bounds(image)
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            print(pixels[(x, y) in image], end="")
        print()


def enhance(image):
    new_image = set()
    xmin, xmax, ymin, ymax = image_bounds(image)
    for y in range(ymin - 3, ymax + 4):
        for x in range(xmin - 3, xmax + 4):
            if enhance_pixel(x, y, image):
                new_image.add((x, y))
    return new_image



enhance_pixel(-1000, -1000, image)
for _ in range(3):
    render(image)
    image = enhance(image)
    print("")

render(image)
print(len(image))
