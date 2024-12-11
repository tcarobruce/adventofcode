import sys
from util import readints
from functools import cache

stones = readints(open(sys.argv[1]).read())

@cache
def stones_after(n, i):
    if i == 0:
        return 1
    elif n == 0:
        return stones_after(1, i - 1)
    elif (sl := len(ss := str(n))) % 2 == 0:
        m = sl // 2
        return (
            stones_after(int(ss[:m]), i - 1) +
            stones_after(int(ss[m:]), i - 1)
        )
    else:
        return stones_after(n * 2024, i - 1)


print(sum([stones_after(n, 25) for n in stones]))
print(sum([stones_after(n, 75) for n in stones]))
