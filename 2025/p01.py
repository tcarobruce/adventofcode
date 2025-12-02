import sys

pos = 50
ct = 0

for ln in open(sys.argv[1]).read().split():
    pos = (pos + {"L": -1, "R": 1}[ln[0]] * int(ln[1:])) % 100
    ct += pos == 0

print(ct)


