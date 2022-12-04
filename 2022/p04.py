import sys

lines = [ln.strip().split(",") for ln in open(sys.argv[1])]
contain = 0
overlap = 0
for a, b in lines:
    al, ah = [int(c) for c in a.split("-")]
    bl, bh = [int(c) for c in b.split("-")]
    if (al <= bl and ah >= bh) or (al >= bl and ah <= bh):
        contain += 1
    if (ah >= bl and al <= bh) or (al <= bh and ah >= bl):
        overlap += 1

print(contain)
print(overlap)
