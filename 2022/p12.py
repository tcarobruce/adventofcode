import sys
from collections import deque

grid = {}
start = end = None
for y, line in enumerate(open(sys.argv[1]).read().splitlines()):
    for x, c in enumerate(line):
        if c == "S":
            start = (x, y)
            c = 'a'
        elif c == "E":
            end = (x, y)
            c = 'z'
        grid[(x, y)] = ord(c) - ord('a')


def neighbors(pos):
    x, y = pos
    yield (x - 1, y)
    yield (x, y - 1)
    yield (x + 1, y)
    yield (x, y + 1)


def find_path_length(start):
    q = deque([(0, start)])
    visited = set(start)

    while q:
        steps, pos = q.popleft()
        if pos == end:
            return steps

        height = grid[pos]

        for n in neighbors(pos):
            if n in visited:
                continue
            nheight = grid.get(n)
            if nheight is None:  # outside grid
                continue
            if nheight - height > 1:
                continue
            visited.add(n)
            q.append((steps + 1, n))


print(find_path_length(start))
all_paths = [find_path_length(s) for s, h in grid.items() if h == 0]
print(min([p for p in all_paths if p is not None]))
