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


grid = {}
for y, ln in enumerate(warehouse.split("\n")):
    for x, c in enumerate(ln):
        x *= 2
        v1 = V(x, y)
        v2 = V(x + 1, y)
        if c in "#.":
            grid[v1] = grid[v2] = c
        elif c == "@":
            grid[v1] = "@"
            robot = v1
            grid[v2] = "."
        elif c == "O":
            grid[v1] = "["
            grid[v2] = "]"

def can_move(pos, d):
    c = grid.get(pos + d)
    if c == ".":
        return set([pos])
    if c == "#":
        return None
    if c in "[]":
        one = can_move(pos + d, d)
        if d.els[0]:
            if one is not None:
                return set([pos]) | one
        else:
            flip = {"[": V(1, 0), "]": V(-1, 0)}
            other = can_move(pos + d + flip[c], d)
            if one is not None and other is not None:
                return set([pos]) | one | other

def shift2(start, d):
    pos = start
    moves = can_move(pos, d)
    if moves is None:
        return start
    to_move = {}
    for m in moves:
        to_move[m] = grid.pop(m)
        grid[m] = '.'
    for m in moves:
        grid[m + d] = to_move[m]
    grid[start] = '.'
    return start + d


maxx = max([v.els[0] for v in grid])
maxy = max([v.els[1] for v in grid])

def draw():
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            print(grid[V(x, y)], end="")
        print()



#print("Initial state:")
#draw()
for i in instructions:
    d = dirs[i]
    robot = shift2(robot, d)
    #print()
    #print(f"Move {i}:")
    #draw()
    #input()


total = 0
for v, c in grid.items():
    if c == "[":
        total += v.els[0] + 100 * v.els[1]
print(total)


