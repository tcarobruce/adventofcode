import sys

tot = 0
for ln in open(sys.argv[1]):
    digs = []
    for c in ln.strip():
        if c.isdigit():
            digs.append(int(c))
    tot += 10 * digs[0] + digs[-1]

print(tot)
