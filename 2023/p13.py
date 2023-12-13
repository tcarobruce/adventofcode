import os
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
            yield i

def find_reflection_vert(lines):
    lines = rot_right(lines)
    #print("rot\n" + "\n".join(lines))

    yield from find_reflection_horiz(lines)

def find_reflections(lines):
    for reflection in find_reflection_horiz(lines):
        yield True, reflection
    for reflection in find_reflection_vert(lines):
        yield False, reflection

# def find_reflection(lines):
#     h = find_reflection_horiz(lines)
#     if h:
#         return 100 * h
#     return find_reflection_vert(lines)


def perturb(lines):
    m = {"#": ".", ".": "#"}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            nl = line[:j] + m[c] + line[j+1:]
            yield lines[:i] + [nl] + lines[i+1:]

# for pattern in patterns:
#     lines = pattern.split()
#     for i, modification in enumerate(perturb(lines)):
#         os.system("clear")
#         print(f"ORIG {len(lines[0])} x {len(lines)} = {len(lines[0]) * len(lines)}")
#         print("\n".join(lines))
#         print(i)
#         print("\n".join(modification))
#         input()

# lines = """
# ..##..##...
# ..#.##.#.##
# ...#.#.#...
# ##.#.####..
# ...###.#.##
# ######.#.##
# ######..#.#
# """.strip().split()

# #print(find_reflection(lines))

# for i, modification in enumerate(perturb(lines)):
#     os.system("clear")
#     print(f"ORIG {len(lines[0])} x {len(lines)} = {len(lines[0]) * len(lines)}")
#     print("\n".join(lines))
#     print(i)
#     print("\n".join(modification))
#     print()
#     print("\n".join(rot_right(modification)))
#     #print(find_reflection(modification))
#     input()

tot = 0
p2_tot = 0
for i, pattern in enumerate(patterns):
    lines = pattern.split()
    r = next(find_reflections(lines))
    horiz, divider = r
    #print(pattern, r)
    tot += (100 if horiz else 1) * divider

    done = False
    for modification in perturb(lines):
        for nr in find_reflections(modification):
            if nr == r:
                continue
            n_horiz, n_divider = nr
            p2_tot += (100 if n_horiz else 1) * n_divider
            done = True
            break
        if done:
            break
    else:
        print(f"NONE FOUND FOR {i}:\n" + "\n".join(lines))
        foom


print(tot)
print(p2_tot)

