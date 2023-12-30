import sys
from util import Vec as V
from collections import deque
from PIL import Image, ImageDraw, ImageFont


G = {}
S = None

for y, ln in enumerate(open(sys.argv[1])):
    for x, c in enumerate(ln.strip()):
        v = V(x, y)
        if c == "S":
            S = v
            c = "."
        G[v] = c

SIZE = v + V(1, 1)

def get_grid(v):
    return G.get(V(v.els[0] % SIZE.els[0], v.els[1] % SIZE.els[1]))

def draw(ext, reached):
    for y in range(ext[0].els[1], ext[1].els[1] + 1):
        for x in range(ext[0].els[0], ext[1].els[0] + 1):
            v = V(x, y)
            if v in reached:
                c = "O"
            else:
                c = get_grid(v)
                if c == '.':
                    c = ' '
            print(c, end="")
        print()


def draw(ext, reached, steps):
    img = Image.new('RGB', (ext[1] - ext[0] + V(1, 1)).els)
    for y in range(ext[0].els[1], ext[1].els[1] + 1):
        for x in range(ext[0].els[0], ext[1].els[0] + 1):
            v = V(x, y)
            c = None
            if v in reached:
                c = (255, 127, 0)
            else:
                if get_grid(v) == '.':
                    c = (255, 255, 255)
            if c is not None:
                xy = (v - ext[0]).els
                img.putpixel(xy, c)
    I1 = ImageDraw.Draw(img)
    font = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf', 24)
    I1.text((10, 10), str(steps), fill=(0, 120, 200), font=font)
    img.show()


def walk(start):
    q = deque([(0, start)])
    reached = [set(), set()]

    last = 0
    while q:
        #print(q, len(right_dist))
        steps, pos = q.popleft()
        if steps != last:
            yield last, reached[last % 2]
            last = steps
        if get_grid(pos) != ".":
            continue
        mod = steps % 2
        if pos in reached[mod]:
            continue
        reached[mod].add(pos)
        q.extend([(steps + 1, p) for p in pos.neighbors()])


s = 400
ext = S - V(s, s), S + V(s, s)
from os import system
results = {}
for steps, r in walk(S):
    l = len(r)
    results[steps] = l
    if steps and (steps - 65) % 262 == 0:
        #draw(ext, r, steps)
        d = (steps - 65) // 131
        a, b = V.extent(r)
        a -= V(65, 65)
        b -= V(65, 65)
        print(d, steps, l, b.els[0] - a.els[0])
