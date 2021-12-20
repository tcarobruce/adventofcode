import sys

lines = (ln.strip() for ln in open(sys.argv[1]))

iea_string = next(lines)
next(lines)

image = {}
for y, ln in enumerate(lines):
    for x, c in enumerate(ln):
        image[(x, y)] = (c == '#')


def neighbors(x, y):
    for j in range(-1, 2):
        for i in range(-1, 2):
            yield x + i, y + j


def enhance_pixel(x, y, image, default=False):
    n = 0
    for xx, yy in neighbors(x, y):
        if image.get((xx, yy), default):
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
            print(pixels[image.get((x, y))], end="")
        print()


def enhance(image, default=False):
    new_image = {}
    xmin, xmax, ymin, ymax = image_bounds(image)
    for y in range(ymin - 2, ymax + 3):
        for x in range(xmin - 2, xmax + 3):
            new_image[(x, y)] = enhance_pixel(x, y, image, default=default)
    return new_image


default = False

for i in range(50):
    if i == 2:
        print(sum(image.values()))
    #render(image)
    image = enhance(image, default=default)
    default = not default  # turn off for test

print(sum(image.values()))
