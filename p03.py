import sys

lines = [ln.strip() for ln in open(sys.argv[1])]
bitwidth = len(lines[0])
nums = [int(ln, 2) for ln in lines]

def most_common(nums, mask):
    return int(sum([bool(num & mask) for num in nums]) * 2 >= len(nums))

# part 1
ge = [0, 0]

mask = 1 << (bitwidth - 1)
while mask:
    mc = most_common(nums, mask)
    ge[mc] ^= mask
    mask >>= 1

print(ge[0] * ge[1])
# 841526

# part 2

def apply_bit_criteria(nums, least=False):
    mask = 1 << (bitwidth - 1)
    while len(nums) > 1:
        mc = most_common(nums, mask)
        if least:
            mc = 1 - mc
        nums = {num for num in nums if bool(num & mask) == mc}
        mask >>= 1
    return nums.pop()

oxygen = apply_bit_criteria(set(nums))
co2 = apply_bit_criteria(set(nums), least=True)

print(co2 * oxygen)
# 4790390
