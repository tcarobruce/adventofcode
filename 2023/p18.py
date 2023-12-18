import sys
import re
from util import Vec as V

lines = [ln.strip() for ln in open(sys.argv[1])]
p = re.compile(r"([RLDU]) (\d+) \(#([a-f0-9]{6})\)")


dirs = {
    "R": V(1, 0),
    "L": V(-1, 0),
    "U": V(0, -1),
    "D": V(0, 1),
}

def outline(lines):
    pos = V(0, 0)
    G = {pos: None}
    for line in lines:
        direction, count, color = p.match(line).groups()
        v = dirs[direction]
        for _ in range(int(count)):
            pos = pos + v
            G[pos] = color
    return G


def find_fill(G):
    mins, maxs = V.extent(G.keys())
    for x in range(mins.els[0], maxs.els[0]):
        for y in range(mins.els[1], maxs.els[1]):
            start = p = V(x, y)
            if start in G:
                continue
            F = dict(G)
            q = [p]
            outside = False
            while q:
                p = q.pop(0)
                if not p.in_extent(mins, maxs):
                    break
                if p in F:
                    continue
                F[p] = 1
                q.extend([p + v for v in dirs.values()])
            else:
                print(start)
                return len(F)


print(find_fill(outline(lines)))

