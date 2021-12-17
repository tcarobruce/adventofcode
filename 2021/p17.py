


test = dict(x=range(20, 31), y=range(-10, -4))
prob = dict(x=range(150, 194), y=range(-136, -85))


def fire_probe(dx, dy, target):
    maxy = 0
    x, y = 0, 0
    overx, overy = max(target['x']), max(target['y'])

    while True:
        if x in target['x'] and y in target['y']:
            return maxy
        elif x > overx or y < overy:
            return None

        x += dx
        y += dy
        maxy = max(maxy, y)
        if dx:
            dx -= 1
        dy -= 1

#print(fire_probe(7, 2, test))
#print(fire_probe(6, 9, test))

maxmaxy = 0
for dx in range(1000):
    for dy in range(1000):
        r = fire_probe(dx, dy, prob)
        if r is not None and r > maxmaxy:
            maxmaxy = r
            print(dx, dy, r)

print(maxmaxy)


