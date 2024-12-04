import sys
from util import Vec as V

grid = {}
xs = []
for y, ln in enumerate(open(sys.argv[1])):
    for x, c in enumerate(ln.strip()):
        grid[V(x, y)] = c
        if c == 'X':
            xs.append(V(x, y))


dirs = list(V(0, 0).neighbors_diag())

def find_xmas(start):
    total = 0
    for dir in dirs:
        if find_xmas_dir(start, dir):
            total += 1
    return total

def find_xmas_dir(pos, dir, remaining="XMAS"):
    if not remaining:
        return True
    elif grid.get(pos) != remaining[0]:
        return False
    else:
        return find_xmas_dir(pos + dir, dir, remaining[1:])


print(sum([find_xmas(xx) for xx in xs]))
