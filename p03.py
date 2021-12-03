import sys

lines = [
    tuple([int(i) for i in ln.strip()]) for ln in open(sys.argv[1])
]

def to_int(ar):
    return int(''.join([str(bit) for bit in ar]), 2)

def most_common(nums, bit):
    return int(sum([num[bit] for num in nums]) * 2 >= len(nums))

# part 1
gamma, epsilon = [], []

for i, _ in enumerate(lines[0]):
    mc = most_common(lines, i)
    gamma.append(mc)
    epsilon.append(1 - mc)


print(to_int(gamma) * to_int(epsilon))
# 841526

# part 2

def apply_bit_criteria(nums, least=False):
    bit = 0
    while len(nums) > 1:
        mc = most_common(nums, bit)
        if least:
            mc = 1 - mc
        nums = {num for num in nums if num[bit] == mc}
        bit += 1
    return nums.pop()

oxygen = to_int(apply_bit_criteria(set(lines)))
co2 = to_int(apply_bit_criteria(set(lines), least=True))

print(co2 * oxygen)
# 4790390
