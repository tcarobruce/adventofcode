import sys

plays = [ln.strip().split(" ") for ln in open(sys.argv[1])]

results = [3, 6, 0]

def score_row(row):
    theirs, mine = row
    my_index = "XYZ".index(mine)
    result = my_index - "ABC".index(theirs)
    return my_index + 1 + (results[result % 3])


print(sum([score_row(p) for p in plays]))  # 13221
