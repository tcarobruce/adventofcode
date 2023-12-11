import sys

lines = [ln.strip() for ln in open(sys.argv[1])]

def expand(image):
    to_expand_x = set(range(len(image[0])))
    for ln in image:
        for x, c in enumerate(ln):
            if c != ".":
                to_expand_x.discard(x)
    expanded_x = []
    for ln in image:
        new_line = ""
        for x, c in enumerate(ln):
            if x in to_expand_x:
                new_line += "."
            new_line += c
        expanded_x.append(new_line)
    expanded_y = []
    for ln in expanded_x:
        if set(ln) == {"."}:
            expanded_y.append(ln)
        expanded_y.append(ln)
    return expanded_y


def neighbors_constrained(loc):
    x, y = loc
    if y > 0:
        yield (x, y - 1)
    if x < len(lines[0]) - 1:
        yield (x + 1, y)
    if y < len(lines) - 1:
        yield (x, y + 1)
    if x > 0:
        yield (x - 1, y)


def shortest_paths(image):
    galaxies = []
    for y, ln in enumerate(image):
        for x, c in enumerate(ln):
            if c == "#":
                galaxies.append((x, y))

    total = 0
    for i, galaxy in enumerate(galaxies):
        for j, other in enumerate(galaxies[i:]):
            dist = abs(galaxy[0] - other[0]) + abs(galaxy[1] - other[1])
            print(i, j, dist)
            total += dist
    return total


print(shortest_paths(expand(lines)))
