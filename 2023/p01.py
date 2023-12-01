import sys
import re

lines = [ln.strip() for ln in open(sys.argv[1])]

words = "one|two|three|four|five|six|seven|eight|nine"
word_map = {w: str(i) for i, w in enumerate(words.split("|"), 1)}

def replace(m):
    return word_map[m.group(0)]

tot = 0
for ln in lines:
    orig = ln
    ln = re.sub(f"({words})", replace, ln)
    digs = []
    for c in ln.strip():
        if c.isdigit():
            digs.append(int(c))
    line_sum = 10 * digs[0] + digs[-1]
    print(orig, ln, line_sum)
    tot += line_sum

print(tot)
