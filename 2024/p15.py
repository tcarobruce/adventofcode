import sys

from util import Vec as V, readints, readgridv

warehouse, instructions = open(sys.argv[1]).read().split("\n\n")

grid = readgridv(warehouse.split("\n"))
instructions = "".join(instructions.split("\n"))


dirs = {
    "<": V(-1, 0),
    "^": V(0, -1),
    ">": V(1, 0),
    "v": V(0, 1),
}

robot = [v for v, c in grid.items() if c == "@"][0]


def shift(start, d):
    q = []
    pos = start
    while grid.get(pos) in "O@":
        q.append(pos)
        pos = pos + d
    c = grid.get(pos)
    if c == ".":
        for p in q[::-1]:
            grid[pos] = grid[p]
            pos = pos - d
        grid[start] = '.'
        return start + d
    else:
        assert c == "#"
        return start


for i in instructions:
    d = dirs[i]
    robot = shift(robot, d)


total = 0
for v, c in grid.items():
    if c == "O":
        total += v.els[0] + 100 * v.els[1]
print(total)
