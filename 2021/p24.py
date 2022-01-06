import sys
from functools import lru_cache
'''
inp a - Read an input value and write it to variable a.
add a b - Add the value of a to the value of b, then store the result in variable a.
mul a b - Multiply the value of a by the value of b, then store the result in variable a.
div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.
'''

lines = [ln.strip().split() for ln in open(sys.argv[1])]
lets = "wxyz"


def get_func(line):
    op = line[0]
    v1 = lets.index(line[1])
    v2 = line[2]
    is_index = v2 in lets
    if is_index:
        v2 = lets.index(v2)
    else:
        v2 = int(v2)

    if op == "add":
        if is_index:
            def fn(vals):
                vals[v1] += vals[v2]
        else:
            def fn(vals):
                vals[v1] += v2

    elif op == "mul":
        if is_index:
            def fn(vals):
                vals[v1] *= vals[v2]
        else:
            def fn(vals):
                vals[v1] *= v2

    elif op == "div":
        if is_index:
            def fn(vals):
                x = vals[v2]
                assert x != 0
                vals[v1] //= x
        else:
            def fn(vals):
                assert v2 != 0
                vals[v1] //= v2

    elif op == "mod":
        if is_index:
            def fn(vals):
                x = vals[v1]
                y = vals[v2]
                assert x >= 0
                assert y > 0
                vals[v1] = x % y
        else:
            def fn(vals):
                x = vals[v1]
                assert x >= 0
                assert v2 > 0
                vals[v1] = vals[v1] % v2

    elif op == "eql":
        if is_index:
            def fn(vals):
                vals[v1] = int(vals[v1] == vals[v2])
        else:
            def fn(vals):
                vals[v1] = int(vals[v1] == v2)
    return fn

def get_function_groups(lines):
    groups = []
    group = []
    for line in lines:
        op = line[0]

        if op == "inp":
            if group:
                groups.append(group)
                group = []
            continue

        group.append(get_func(line))

    if group:
        groups.append(group)
    return groups

func_groups = get_function_groups(lines)


def apply(group_idx, digit, z):
    group = func_groups[group_idx]
    vals = [digit, 0, 0, z]
    for fn in group:
        fn(vals)
    return vals[3]


def apply_all(n):
    digits = (int(c) for c in str(n))
    z = 0
    for i, _ in enumerate(func_groups):
        z = apply(i, next(digits), z)
    return(z)


print(apply_all(51121176121391))
print(apply_all(91897399498995))


digits = list(range(1, 10))
p1 = list(reversed(digits))  # largest first
p2 = digits
active = p2


desired = {0: ()}
group_count = len(func_groups) - 1
for group in range(group_count, -1, -1):
    new_desired = {}
    in_zs = range(1000000)
    if group == 0:
        in_zs = [0]
    for in_z in in_zs:
        for d in active:
            out_z = apply(group, d, in_z)
            if out_z in desired and in_z not in new_desired:
                #print(out_z, in_z, desired[out_z], d)
                new_desired[in_z] = (d,) + desired[out_z]
    desired = new_desired
    print(group, len(desired))

if len(desired) == 1:
    result = int(''.join(str(d) for d in list(desired.values())[0]))
    print("result:", result)
    print("applied:", apply_all(result))
    assert apply_all(result) == 0

else:
    print("More than one result!")
    print(desired)


# p1 (largest): 91897399498995
# p2 (smallest): 51121176121391
