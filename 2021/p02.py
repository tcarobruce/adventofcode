import sys
dirs = [ln.strip().split() for ln in open(sys.argv[1])]

# part 1

depth, horiz = 0, 0
for instruction, amt in dirs:
    amt = int(amt)
    if instruction == "forward":
        horiz += amt
    if instruction == "up":
        depth -= amt
    if instruction == "down":
        depth += amt

print(horiz * depth)

# part 2

depth, horiz, aim = 0, 0, 0
for instruction, amt in dirs:
    amt = int(amt)
    if instruction == "forward":
        horiz += amt
        depth += aim * amt
    if instruction == "up":
        aim -= amt
    if instruction == "down":
        aim += amt

print(horiz * depth)
