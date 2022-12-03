import sys

plays = [ln.strip().split(" ") for ln in open(sys.argv[1])]

abc = "ABC"
xyz = "XYZ"

scores = {"X": 1, "Y": 2, "Z": 3}
results = [3, 6, 0]

def score_row(row):
    theirs, mine = row
    result = xyz.index(mine) - abc.index(theirs)
    return scores[mine] + (results[result % 3])



tot = 0
for p in plays:
    s = score_row(p)
    print(p, s)
    tot += s

print(tot)

