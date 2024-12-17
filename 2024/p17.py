import sys
from util import readints

lines = list(open(sys.argv[1]))
A = readints(lines[0])[0]
B = readints(lines[1])[0]
C = readints(lines[2])[0]

program = readints(lines[4])


pointer = 0
out = []
while pointer < len(program):
    ins = program[pointer]
    opr = program[pointer + 1]
    combo = {4: A, 5: B, 6: C}.get(opr, opr)

    if ins == 0:
        A = A // 2**combo

    elif ins == 1:
        B = B ^ opr

    elif ins == 2:
        B = combo % 8

    elif ins == 3 and A != 0:
        pointer = opr
        continue

    elif ins == 4:
        B = B ^ C

    elif ins == 5:
        out.append(str(combo % 8))

    elif ins == 6:
        B = A // 2**combo

    elif ins == 7:
        C = A // 2**combo

    pointer += 2

print(",".join(out))
