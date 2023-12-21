import sys
from util import Vec as V
from collections import deque


G = {}
S = None

for y, ln in enumerate(open(sys.argv[1])):
    for x, c in enumerate(ln.strip()):
        v = V(x, y)
        if c == "S":
            S = v
            c = "."
        G[v] = c


def walk(start, max_steps):
    q = deque([(0, start)])
    reached = [set(), set()]

    while q:
        #print(q, len(right_dist))
        steps, pos = q.popleft()
        if G.get(pos) != ".":
            continue
        mod = (max_steps - steps) % 2
        if pos in reached[mod]:
            continue
        reached[mod].add(pos)
        if steps < max_steps:
            q.extend([(steps + 1, p) for p in pos.neighbors()])
    return len(reached[0])

print(walk(S, 6))
print(walk(S, 64))
