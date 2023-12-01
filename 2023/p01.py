import sys
import re

lines = [ln.strip() for ln in open(sys.argv[1])]

digits = "|".join([str(d) for d in range(1, 10)])
words = "one|two|three|four|five|six|seven|eight|nine"
word_map = {w: i for i, w in enumerate(words.split("|"), 1)}

def val(m):
    if m.isdigit():
        return int(m)
    else:
        return word_map[m]

tot = 0
patt = re.compile(f"({digits}|{words})")
revpatt = re.compile(f"({digits}|{words[::-1]})")
for ln in lines:
    orig = ln
    first = patt.search(ln).group(0)
    last = revpatt.search(ln[::-1]).group(0)[::-1]
    first_val = val(first)
    last_val = val(last)
    line_sum = 10 * first_val + last_val
    print(ln, first, first_val, last, last_val, line_sum)
    tot += line_sum

print(tot)
