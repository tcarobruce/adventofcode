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
    seen = {(start, facing): 0}
    q = [(score, start, facing)]

    while True:
        score, pos, facing = heappop(q)
        if grid.get(pos) == "E":
            return score
        if grid.get(pos + facing) == 'E':
            return score + 1

        if grid.get(pos + facing) in '.':
            k = (pos + facing, facing)
            new_score = score + 1
            seen_k = seen.get(k)
            if seen_k is None or seen_k > new_score:
                heappush(q, (new_score, pos + facing, facing))
                seen[k] = new_score

        ccw = dirs[(dirs.index(facing) - 1) % 4]
        cw = dirs[(dirs.index(facing) + 1) % 4]

        new_score = score + 1000

        k = (pos, ccw)
        seen_k = seen.get(k)
        if seen_k is None or seen_k > new_score and grid.get(pos + ccw) != "#":
            heappush(q, (new_score, pos, ccw))
            seen[k] = new_score

        k = (pos, cw)
        seen_k = seen.get(k)
        if seen_k is None or seen_k > new_score and grid.get(pos + cw) != "#":
            heappush(q, (score + 1000, pos, cw))
            seen[k] = new_score

        if 0:
            draw(grid, q, seen)
            print(q[0][0])
            input()



print(best_path(grid))
