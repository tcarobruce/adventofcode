import sys
from util import Vec as V, readints
from itertools import combinations


def cross(a, b):
    assert a.dims == b.dims == 2
    return a.els[0] * b.els[1] - a.els[1] * b.els[0]

lines = [ln.strip() for ln in open(sys.argv[1])]
asints = [readints(ln) for ln in lines]


hailstones_2d = [(V(*ints[:2]), V(*ints[3:5])) for ints in asints]
hailstones_3d = [(V(*ints[:3]), V(*ints[3:])) for ints in asints]

#intersection_window = (7, 27)
intersection_window = (200000000000000, 400000000000000)

# to test if p + tr intersects with q + us
#    t = (q − p) × s / (r × s)
#

def forward_intersect(a, b, window):
    p, r = a
    q, s = b
    num = cross((q - p), s)
    den = cross(r, s)
    if den == 0:
        if num == 0:
            print("SAME LINES")
            foom
        return False

    t = num / den
    u = cross((q - p), r) / den
    i = p + (r * t)
    in_window = all([(window[0] <= el <= window[1]) for el in i.els])
    return t > 0 and u > 0 and in_window

for a, b in combinations(hailstones_2d, 2):
    if forward_intersect(a, b, intersection_window):
        print(a, b)

print(sum([
    forward_intersect(a, b, intersection_window)
    for a, b in combinations(hailstones_2d, 2)
]))

