import sys
from util import Vec as V, readgridv
from heapq import heappop, heappush

grid = readgridv(open(sys.argv[1]).readlines())

def best_paths(grid):
    score = 0
    start = [pos for pos, c in grid.items() if c == "S"][0]
    facing = V(1, 0)

    q = [(score, start, facing, [start])]
    seen = {(start, facing): [score, set([start])]}
    winning_score = None
    winning_nodes = set()

    while q:
        score, pos, facing, path = heappop(q)
        if grid.get(pos) == "E":
            if winning_score is None:
                winning_score = score
            elif score > winning_score:
                break
            winning_nodes.update(path)
            continue

        t = seen.get((pos, facing))
        if t is not None:
            seen_score, seen_set = t
            if seen_score < score:
                continue
            elif seen_score == score:
                seen_set.update(path)
            else:
                seen[(pos, facing)] = score, set(path)
        else:
            seen[(pos, facing)] = score, set(path)

        n = pos + facing
        if grid.get(n) in '.E':
            heappush(q, (score + 1, n, facing, path + [n]))

        cw = facing.rotate_cw()
        if grid.get(pos + cw) in '.E':
            heappush(q, (score + 1000, pos, cw, path))

        ccw = facing.rotate_ccw()
        if grid.get(pos + ccw) in '.E':
            heappush(q, (score + 1000, pos, ccw, path))

    return winning_score, winning_nodes


score, nodes = best_paths(grid)
print(score)
print(len(nodes))
