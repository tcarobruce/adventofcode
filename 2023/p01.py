import sys

lines = [ln.strip() for ln in open(sys.argv[1])]

words = "zero, one, two, three, four, five, six, seven, eight, nine".split(", ")
word_map = {w: i for i, w in enumerate(words)}

tot = 0
for ln in lines:
    orig = ln
    for w, d in word_map.items():
        ln = ln.replace(w, str(d))
    digs = []
    for c in ln.strip():
        if c.isdigit():
            digs.append(int(c))
    line_sum = 10 * digs[0] + digs[-1]
    print(orig, ln, line_sum)
    tot += line_sum

print(tot)

