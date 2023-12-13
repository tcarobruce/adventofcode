import sys

patterns = open(sys.argv[1]).read().split("\n\n")

def rot_right(lines):
    out = []
    for i in range(len(lines[0])):
        out.append("".join([ln[i] for ln in lines]))
    return out

def find_reflection_horiz(lines):
    length = len(lines)
    for i in range(1, len(lines)):
        left = lines[max(0, (2 * i) - length):i]
        right = lines[2 * i - 1:i-1:-1]
        #print(i, left, right)
        if left == right:
            return i

def find_reflection_vert(lines):
    lines = rot_right(lines)
    #print("rot\n" + "\n".join(lines))

    return find_reflection_horiz(lines)

def find_reflection(pattern):
    lines = pattern.split()
    h = find_reflection_horiz(lines)
    if h:
        return 100 * h
    return find_reflection_vert(lines)

tot = 0
for pattern in patterns:
    r = find_reflection(pattern)
    #print(pattern, r)
    tot += r

print(tot)
