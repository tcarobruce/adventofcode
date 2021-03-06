import sys
nums = [int(ln.strip()) for ln in open(sys.argv[1])]

# part 1
print(sum([b > a for a, b in zip(nums[:-1], nums[1:])]))

# part 2
print(sum([b > a for a, b in zip(nums[:-3], nums[3:])]))
