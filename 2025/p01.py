import sys

pos = 50
ct = ct2 = 0

for ln in open(sys.argv[1]).read().split():
    last = pos
    rotation = {"L": -1, "R": 1}[ln[0]] * int(ln[1:])
    d, pos = divmod(pos + rotation, 100)
    ct += pos == 0

    if d < 0 and last == 0 and pos != 0:
        d += 1
    if d > 0 and pos == 0:
        d -= 1
    ct2 += abs(d) + (pos == 0)

    print(last, ln, pos, ct, ct2)


print(ct)
print(ct2)

