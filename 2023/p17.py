import sys
from util import Vec as V
from heapq import heappush, heappop

G = {}
for y, ln in enumerate(open(sys.argv[1])):
    for x, c in enumerate(ln.strip()):
        G[V(x, y)] = int(c)

dest = V(x, y)


def traverse(low, high):
    q = [(0, V(0, 0), vel) for vel in [V(1, 0), V(0, 1)]]
    seen = set()

    while True:
        #print(q)
        heat_loss, pos, velocity = heappop(q)
        if pos == dest:
            return heat_loss

        if (pos, velocity) in seen:
            continue
        seen.add((pos, velocity))

        for v in [velocity.rotate_cw(), velocity.rotate_ccw()]:
            hlt = heat_loss
            np = pos
            for i in range(1, high):
                np += v
                hl = G.get(np)
                if hl is None:
                    break
                hlt += hl
                if i >= low:
                    heappush(q, (hlt, np, v))

print(traverse(1, 4))
print(traverse(4, 11))
