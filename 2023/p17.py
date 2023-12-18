import sys
from util import Vec as V
from heapq import heappush, heappop

G = {}
for y, ln in enumerate(open(sys.argv[1])):
    for x, c in enumerate(ln.strip()):
        G[V(x, y)] = int(c)

dest = V(x, y)


def traverse():
    q = [(0, V(0, 0), vel, 0) for vel in [V(1, 0), V(0, 1)]]
    seen = set()

    while True:
        print(q[0])
        heat_loss, pos, velocity, conseq = heappop(q)
        if pos == dest:
            return heat_loss

        if (pos, velocity, conseq) in seen:
            continue
        seen.add((pos, velocity, conseq))

        if conseq < 3:
            np = pos + velocity
            hl = G.get(np)
            if hl is not None:
                heappush(q, (heat_loss + hl, np, velocity, conseq + 1))

        for nv in [velocity.rotate_cw(), velocity.rotate_ccw()]:
            np = pos + nv
            hl = G.get(np)
            if hl is not None:
                heappush(q, (heat_loss + hl, np, nv, 1))


print(traverse())
