import sys
lines = (ln.strip() for ln in open(sys.argv[1]))

def check_line(line):
    s = []
    pairs = ("()", "[]", "{}", "<>")
    paired = {b: a for a, b in pairs}

    for c in line:
        if c in '([{<':
            s.append(c)
        elif c in ')]}>':
            if s and s[-1] == paired[c]:
                s.pop()
            else:
                return "corrupt", c
    if s:
        return "incomplete", ""
    else:
        return "complete", ""



scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

total = 0
for ln in lines:
    result, c = check_line(ln)
    if result == "corrupt":
        total += scores[c]

# part 1: 388713
print(total)




