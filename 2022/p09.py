import sys

lines = open(sys.argv[1]).read().splitlines()

def move(p, direction):
    if direction == "R":
        return (p[0] + 1, p[1])
    if direction == "L":
        return (p[0] - 1, p[1])
    if direction == "U":
        return (p[0], p[1] + 1)
    if direction == "D":
        return (p[0], p[1] - 1)

def follow(h, t):
    # return new tail position
    dist = abs(h[0] - t[0]) + abs(h[1] - t[1])
    if dist <= 1:
        return t
    if dist == 2:
        if h[0] != t[0] and h[1] != t[1]:
            return t
        elif h[0] == t[0]:
            return (t[0], (h[1] + t[1]) // 2)
        elif h[1] == t[1]:
            return ((h[0] + t[0]) // 2, t[1])
        else:
            assert False, "Unexpected positions %s %s" % (h, t)
    elif dist == 3:
        if abs(h[0] - t[0]) == 1:
            return (h[0], (h[1] + t[1]) // 2)
        if abs(h[1] - t[1]) == 1:
            return ((h[0] + t[0]) // 2, h[1])
        assert False, "also unexpected positions %s %s" % (h, t)
    elif dist == 4:
        return ((h[0] + t[0]) // 2, (h[1] + t[1]) // 2)
    assert False


def draw_grid(size=6):
    for y in range(size):
        for x in range(size):
            p = (x, size - y - 1)
            if p == rope[0]:
                print("H", end="")
            elif p in rope:
                print(rope.index(p), end="")
            elif p == (0, 0):
                print("s", end="")
            else:
                print(".", end="")
        print()


rope = [(0, 0) for _ in range(10)]
positions1 = {rope[0]}
positions10 = {rope[9]}

for line in lines:
    direction, count = line.split()
    count = int(count)
    for _ in range(count):
        rope[0] = move(rope[0], direction)
        for i in range(9):
            rope[i + 1] = follow(rope[i], rope[i + 1])
        positions1.add(rope[1])
        positions10.add(rope[9])

print(len(positions1))
print(len(positions10))
