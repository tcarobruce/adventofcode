import sys

from util import Vec as V, readints
from math import prod
from time import sleep
from subprocess import run

lines = [readints(ln) for ln in open(sys.argv[1])]

DIMS = V(*((101, 103) if sys.argv[1] == "p14_input.txt" else (11, 7)))
WIDTH, HEIGHT = DIMS.els

robots = [[V(*r[:2]), V(*r[2:])] for r in lines]

def move(r):
    r[0] += r[1]
    r[0] = r[0].wrap(DIMS)


def quad(pos):
    # return 0,1,2,3,None
    x, y = pos.els
    if x < WIDTH // 2:
        if y < HEIGHT // 2:
            return 0
        elif y > HEIGHT // 2:
            return 1
    elif x > WIDTH // 2:
        if y < HEIGHT // 2:
            return 2
        elif y > HEIGHT // 2:
            return 3

def calculate_quads(robots):
    quads = [0] * 4
    for pos, _ in robots:
        q = quad(pos)
        if q is not None:
            quads[q] += 1

    return prod(quads)

def draw(robots):
    positions = set([r[0].els for r in robots])
    img = []
    is_it = False
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            row += ("X" if (x, y) in positions else ".")
        img.append(row)
        if "XXXXXXXXXXXXX" in row:
            is_it = True
    return img, is_it


i = 0
quads = None
while True:
    i += 1
    print(i)
    for r in robots:
        move(r)
    img, is_it = draw(robots)
    if i == 100:
        quads = calculate_quads(robots))
    if is_it:
        print("\n".join(img))
        break

print("QUADS:", quads)
print(i)
