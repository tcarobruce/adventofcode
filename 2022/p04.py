import sys

lines = [ln.strip().split(",") for ln in open(sys.argv[1])]
sections = []
tot = 0
for a, b in lines:
    al, ah = [int(c) for c in a.split("-")]
    bl, bh = [int(c) for c in b.split("-")]
    if (al <= bl and ah >= bh) or (al >= bl and ah <= bh):
        tot += 1
    sections.append(((al, ah), (bl, bh)))

print(sections)
print(tot)
