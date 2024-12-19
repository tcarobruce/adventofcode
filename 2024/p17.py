import sys
from util import readints

lines = list(open(sys.argv[1]))
A = readints(lines[0])[0]
B = readints(lines[1])[0]
C = readints(lines[2])[0]

program = readints(lines[4])


def get_output(a, b, c, program, dbg=False, break_early=False):
    pointer = 0
    out = []
    while pointer < len(program):
        ins = program[pointer]
        opr = program[pointer + 1]
        combo = {4: a, 5: b, 6: c}.get(opr, opr)

        if dbg:
            print(f"A: {a} B: {b} C: {c} pt: {pointer} {ins}/{opr}/{combo}, {out}")
            input()

        if ins == 0:
            a = a // 2**combo

        elif ins == 1:
            b = b ^ opr

        elif ins == 2:
            b = combo % 8

        elif ins == 3 and a != 0:
            pointer = opr
            continue

        elif ins == 4:
            b = b ^ c

        elif ins == 5:
            s = combo % 8
            out.append(s)

        elif ins == 6:
            b = a // 2**combo

        elif ins == 7:
            c = a // 2**combo

        pointer += 2

    return out


a = 0
for i in range(len(program)):
    p = program[-1-i:]
    a = 8 * a
    if a:
        a -= 8
    while True:
        a += 1
        r = get_output(a, B, C, program)
        if r == p:
            print(a, r)
            break

print(a)
print(get_output(a, B, C, program))
print(program)

'''
# suffixes (better!):
5 [0]
43 [3, 0]
47 [3, 0]
346 [5, 3, 0]
378 [5, 3, 0]
2770 [5, 5, 3, 0]
2773 [5, 5, 3, 0]
3026 [5, 5, 3, 0]
22164 [3, 5, 5, 3, 0]
22187 [3, 5, 5, 3, 0]
22188 [3, 5, 5, 3, 0]
24212 [3, 5, 5, 3, 0]
177313 [0, 3, 5, 5, 3, 0]
177503 [0, 3, 5, 5, 3, 0]
177505 [0, 3, 5, 5, 3, 0]
193697 [0, 3, 5, 5, 3, 0]

2 4: B = A % 8
1 2: B = B ^ 2
7 5: C = A // 2**B
1 7: B = B ^ 7
4 4: B = B ^ C
0 3: A = A // 8
5 5: B % 8 -> out
3 0: if A jmp 0
'''
