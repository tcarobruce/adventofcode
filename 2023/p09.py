import sys
from util import readints

lines = [readints(ln) for ln in open(sys.argv[1])]

def find_next(nums):
    if len(set(nums)) == 1:
        return nums[0]
    diffs = [(b - a) for a, b in zip(nums[:-1], nums[1:])]
    return nums[-1] + find_next(diffs)


print(sum([find_next(line) for line in lines]))
