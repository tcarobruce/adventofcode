import sys

from util import Vec as V, readints
from math import prod

lines = [readints(ln) for ln in open(sys.argv[1])]

DIMS = V(*((101, 103) if sys.argv[1] == "p14_input.txt" else (11, 7)))
WIDTH, HEIGHT = DIMS.els

robots = [[V(*r[:2]), V(*r[2:])] for r in lines]

def move(r):
    r[0] += r[1]
    r[0] = r[0].wrap(DIMS)

for _ in range(100):
    for r in robots:
        move(r)


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

quads = [0] * 4
for pos, _ in robots:
    q = quad(pos)
    if q is not None:
        quads[q] += 1

print(quads)
print(prod(quads))

