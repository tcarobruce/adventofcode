import sys

plays = [ln.strip().split(" ") for ln in open(sys.argv[1])]

results = [3, 6, 0]

def score_row(row):
    theirs, mine = row
    my_index = "XYZ".index(mine)
    result = my_index - "ABC".index(theirs)
    return my_index + 1 + (results[result % 3])


print(sum([score_row(p) for p in plays]))  # 13221


offsets = [-1, 0, 1]
results2 = [0, 3, 6]

def score_row2(row):
    theirs, result = row
    result_index = "XYZ".index(result)
    mine = ("ABC".index(theirs) + offsets[result_index]) % 3
    return mine + 1 + results2[result_index]


print(sum([score_row2(p) for p in plays]))  # 13131
