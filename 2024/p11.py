import sys
from util import readints

stones = readints(open(sys.argv[1]).read())

def blink(stones):
    r = []
    for s in stones:
        if s == 0:
            r.append(1)
        elif len(ss := str(s)) % 2 == 0:
            m = len(ss) // 2
            r.append(int(ss[:m]))
            r.append(int(ss[m:]))
        else:
            r.append(s * 2024)
    return r


for i in range(1, 26):
    r = blink(stones)
    print(i, len(r))
    stones = r


