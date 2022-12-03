import sys

plays = [ln.strip().split(" ") for ln in open(sys.argv[1])]

results = [0, 3, 6]

def score_row(theirs, mine):
    my_index = "XYZ".index(mine)
    result_index = my_index - "ABC".index(theirs) + 1
    return my_index + 1 + (results[result_index % 3])


print(sum([score_row(*p) for p in plays]))  # 13221


def score_row2(theirs, result):
    result_index = "XYZ".index(result)
    my_index = ("ABC".index(theirs) + result_index - 1) % 3
    return my_index + 1 + results[result_index]


print(sum([score_row2(*p) for p in plays]))  # 13131
