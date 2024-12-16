import sys
from util import Vec as V, readgridv
from heapq import heappop, heappush

grid = readgridv(open(sys.argv[1]).readlines())


dirs = [V(1, 0), V(0, 1), V(-1, 0), V(0, -1)]
facing = ">v<^"


def draw(grid, q, seen):
    maxx = max([v.els[0] for v in grid])
    maxy = max([v.els[1] for v in grid])
    edge_score, edge, _ = q[0]
    edges = {}
    seen = {t[0] for t in seen}
    for t in q:
        if t[0] == edge_score:
            edges[t[1]] = t[2]
        else:
            break

    for y in range(maxy + 1):
        for x in range(maxx + 1):
            v = V(x, y)
            if v in edges:
                c = facing[dirs.index(edges[v])]
            elif v in seen:
                c = ' '
            else:
                c = grid.get(v)
            print(c, end="")
        print()


def best_path(grid):
    start = [pos for pos, c in grid.items() if c == "S"][0]
    score = 0
    facing = V(1, 0)
    seen = set([(start, facing)])
    q = [(score, start, facing)]

    while True:
        score, pos, facing = heappop(q)
        if grid.get(pos) == "E":
            return score
        if grid.get(pos + facing) == 'E':
            return score + 1

        if grid.get(pos + facing) in '.':
            k = (pos + facing, facing)
            if k not in seen:
                heappush(q, (score + 1, pos + facing, facing))
                seen.add(k)
                seen.add((pos + facing, V(0, 0) - facing))
        ccw = dirs[(dirs.index(facing) - 1) % 4]
        cw = dirs[(dirs.index(facing) + 1) % 4]

        k = (pos, ccw)
        if k not in seen:
            heappush(q, (score + 1000, pos, ccw))
            seen.add(k)

        k = (pos, cw)
        if k not in seen:
            heappush(q, (score + 1000, pos, cw))
            seen.add(k)

        if 0:
            draw(grid, q, seen)
            print(q[0][0])
            input()

print(best_path(grid))
