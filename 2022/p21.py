import sys
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


orig_nums = dict(nums)

def resolve(m):
    v = nums.get(m)
    if v is not None:
        return v
    left, op, right = maths[m]
    return OPS[op](resolve(left), resolve(right))


print(resolve("root"))

nums.pop("humn")
maths["root"][1] = "=="

def reconcile(m, result):
    if m == "humn":
        print(result)
        return None

    left, op, right = maths[m]
    try:
        left_result = resolve(left)
    except:
        left_result = None

    try:
        right_result = resolve(right)
    except:
        right_result = None

    if op == "==":
        if left_result is None:
            reconcile(left, right_result)
        if right_result is None:
            reconcile(right, left_result)

    if op == "+":
        if left_result is None:
            reconcile(left, result - right_result)
        elif right_result is None:
            reconcile(right, result - left_result)

    if op == "*":
        if left_result is None:
            reconcile(left, result // right_result)
        elif right_result is None:
            reconcile(right, result // left_result)

    if op == "-":
        if left_result is None:
            reconcile(left, result + right_result)
        elif right_result is None:
            reconcile(right, left_result - result)

    if op == "/":
        if left_result is None:
            reconcile(left, result * right_result)
        elif right_result is None:
            reconcile(right, left_result // result)


reconcile("root", 0)
