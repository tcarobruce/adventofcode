import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

lines = open(sys.argv[1]).read().splitlines()

G = defaultdict(list)
START = END = None

dirs = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

for y, row in enumerate(lines):
    for x, c in enumerate(row):
        if c == "#":
            continue
        if c == ".":
            if START is None:
                START = (x, y)
            END = (x, y)
            continue

        G[(x, y)].append(c)


WIDTH = x
HEIGHT = y


def open_neighbors(pos, g):
    moves = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    for d in moves:
        p = add(pos, d)
        if p not in g and (p in (START, END) or ((0 < p[0] < WIDTH) and (0 < p[1] < HEIGHT))):
            yield p


def iter(g):
    new_g = defaultdict(list)
    for pos, blizzards in g.items():
        for blizzard in blizzards:
            newx, newy = add(pos, dirs[blizzard])
            newx = (newx - 1) % (WIDTH - 1) + 1
            newy = (newy - 1) % (HEIGHT - 1) + 1
            new_g[(newx, newy)].append(blizzard)
    return new_g


memo = {0: G}
def state_at(i):
    if i not in memo:
        if i - 1 in memo:
            memo[i] = iter(memo[i - 1])
        else:
            memo[i] = state_at(i - 1)
    return memo[i]


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def draw(g, pos):
    for y in range(HEIGHT + 1):
        for x in range(WIDTH + 1):
            p = (x, y)
            if p == pos:
                c = "E"
            elif p in (START, END):
                c = "."
            elif x in (0, WIDTH) or y in (0, HEIGHT):
                c = "#"
            elif p in g:
                if len(g[p]) > 1:
                    c = str(len(g[p]))
                else:
                    c = g[p][0]
            else:
                c = "."
            print(c, end="")
        print()


def find_path_length(start, end, start_minute=0):
    q = [(dist(start, end), start_minute, start)]
    seen = {q[0]}
    while True:
        n = heappop(q)
        cost, minutes, pos = n
        print(cost, minutes, pos, cost - minutes, len(q))
        if 0:
            draw(state_at(minutes), pos)
            print(cost, minutes, pos)
            print()
            input()
        if pos == end:
            return minutes
        minutes += 1
        for new_pos in open_neighbors(pos, state_at(minutes)):
            cost = dist(new_pos, end) + minutes
            n = (cost, minutes, new_pos)
            if n in seen:
                continue
            seen.add(n)
            heappush(q, n)


there = find_path_length(START, END)
print(there)
back = find_path_length(END, START, start_minute=there)
there_again = find_path_length(START, END, start_minute=back)
print(there_again)
