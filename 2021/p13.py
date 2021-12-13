import sys
lines = (ln.strip() for ln in open(sys.argv[1]))

points = set()
for ln in lines:
    if not ln:
        break
    x, y = ln.split(",")
    points.add((int(x), int(y)))

folds = []
for ln in lines:
    assert ln.startswith("fold along ")
    axis, offset = ln[len("fold along "):].split("=")
    folds.append((axis, int(offset)))


def do_fold(points, axis, offset):
    return {
        (
            2 * offset - x if (axis == "x" and x > offset) else x,
            2 * offset - y if (axis == "y" and y > offset) else y
        )
        for x, y in points
    }


def print_points(points):
    xmax = max(x for x, _ in points)
    ymax = max(y for _, y in points)
    for y in range(ymax + 1):
        for x in range(xmax + 1):
            print("#" if (x, y) in points else " ", end="")
        print()


for i, (axis, offset) in enumerate(folds, 1):
    points = do_fold(points, axis, offset)
    if i == 1:
        print(len(points))

print_points(points)
