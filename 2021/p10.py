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
        return "incomplete", s
    else:
        return "complete", s



scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

base_score = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

def complete_stack(stack):
    total = 0
    for c in stack[::-1]:
        total *= 5
        total += base_score[c]
    return total


total = 0
completions = []
for ln in lines:
    result, c = check_line(ln)
    if result == "corrupt":
        total += scores[c]
    elif result == "incomplete":
        completions.append(complete_stack(c))

# part 1: 388713
print(total)

# part 2: 3539961434
completions.sort()
print(completions[len(completions)//2])
