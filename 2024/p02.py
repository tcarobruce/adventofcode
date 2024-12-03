import sys
from util import readints

lines = [readints(ln) for ln in open(sys.argv[1])]

def _is_safe(nums):
    ok = {1,2,3}
    for a, b in zip(nums[:-1], nums[1:]):
        if b - a not in ok:
            return False
    return True

def is_safe(nums):
    return _is_safe(nums) or _is_safe(nums[::-1])

print(len([ln for ln in lines if is_safe(ln)]))

def is_sorta_safe(nums):
    return (
        is_safe(nums) or
        any(is_safe(nums[:i] + nums[i+1:]) for i in range(len(nums)))
    )

print(len([ln for ln in lines if is_sorta_safe(ln)]))
