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
    else:
        assert dist == 3
        if abs(h[0] - t[0]) == 1:
            return (h[0], (h[1] + t[1]) // 2)
        if abs(h[1] - t[1]) == 1:
            return ((h[0] + t[0]) // 2, h[1])
        assert False, "also unexpected positions %s %s" % (h, t)


def draw_grid(size=6):
    for y in range(size):
        for x in range(size):
            p = (x, size - y - 1)
            if p == (0, 0):
                print("s", end="")
            elif p == H:
                print("H", end="")
            elif p == T:
                print("T", end="")
            else:
                print(".", end="")
        print()


H = (0, 0)
T = (0, 0)
positions = {T}

for line in lines:
    direction, count = line.split()
    count = int(count)
    for _ in range(count):
        H = move(H, direction)
        T = follow(H, T)
        positions.add(T)
        #draw_grid()
        #input()

print(len(positions))
