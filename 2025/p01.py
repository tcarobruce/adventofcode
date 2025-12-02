import sys

pos = 50
ct = ct2 = 0

for ln in open(sys.argv[1]).read().split():
    last = pos
    pos = pos + {"L": -1, "R": 1}[ln[0]] * int(ln[1:])

    d, pos = divmod(pos, 100)
    if pos == 0 and d == 0:
        ct2 += 1
    elif last == 0 and d == -1:
        pass
    else:
        ct2 += abs(d)
    print(ln, last, d, pos, ct2)

    if pos == 0:
        ct += 1


print(ct)
print(ct2)
