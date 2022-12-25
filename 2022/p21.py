import sys
from collections import deque
from operator import add, sub, mul, truediv, floordiv

OPS = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": floordiv,
}

lines = open(sys.argv[1]).read().splitlines()

nums = {}
maths = {}

for ln in lines:
    monkey, rest = ln.strip().split(": ")
    if rest.isdigit():
        nums[monkey] = int(rest)
    else:
        maths[monkey] = rest.split()


def resolve(m):
    v = nums.get(m)
    if v is not None:
        return v
    left, op, right = maths[m]
    v = OPS[op](resolve(left), resolve(right))
    nums[m] = v
    return v


print(resolve("root"))
