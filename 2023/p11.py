import sys

lines = [ln.strip() for ln in open(sys.argv[1])]

def expand(image):
    expand_x = set(range(len(image[0])))
    expand_y = set(range(len(image)))
    for y, ln in enumerate(image):
        for x, c in enumerate(ln):
            if c != ".":
                expand_x.discard(x)
                expand_y.discard(y)
    return expand_x, expand_y

def shortest_paths(image, expand_x, expand_y, expansion_factor):
    galaxies = []
    for y, ln in enumerate(image):
        for x, c in enumerate(ln):
            if c == "#":
                galaxies.append((x, y))

    total = 0
    for i, galaxy in enumerate(galaxies):
        for j, other in enumerate(galaxies[i:]):
            dist = abs(galaxy[0] - other[0]) + abs(galaxy[1] - other[1])
            for expand in expand_x:
                if min(galaxy[0], other[0]) < expand < max(galaxy[0], other[0]):
                    dist += expansion_factor - 1
            for expand in expand_y:
                if min(galaxy[1], other[1]) < expand < max(galaxy[1], other[1]):
                    dist += expansion_factor - 1
            total += dist
    return total


expand_x, expand_y = expand(lines)
print(shortest_paths(lines, expand_x, expand_y, 2))
print(shortest_paths(lines, expand_x, expand_y, 10))
print(shortest_paths(lines, expand_x, expand_y, 100))
print(shortest_paths(lines, expand_x, expand_y, 1000000))
