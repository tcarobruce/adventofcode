import sys
lines = (ln.strip() for ln in open(sys.argv[1]))

corrupt_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

completion_scores = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

def score_line(line):
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
                return "corrupt", corrupt_scores[c]
    if s:
        score = 0
        for c in s[::-1]:
            score *= 5
            score += completion_scores[c]
        return "incomplete", score
    else:
        return "complete", None  # shouldn't happen


corrupt_total = 0
completions = []
for ln in lines:
    result, c = score_line(ln)
    if result == "corrupt":
        corrupt_total += c
    elif result == "incomplete":
        completions.append(c)


# part 1: 388713
print(corrupt_total)

# part 2: 3539961434
completions.sort()
print(completions[len(completions)//2])
