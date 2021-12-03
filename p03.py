import sys

lines = [
    tuple([int(i) for i in ln.strip()]) for ln in open(sys.argv[1])
]

# part 1
width = len(lines[0])
totals = [0] * width

for i, ln in enumerate(lines):
    for j, x in enumerate(ln):
        totals[j] += x

gamma, epsilon = [], []

half = i / 2
for bit in totals:
    gamma.append(int(bit > half))
    epsilon.append(int(bit < half))

print(half, totals)
print(gamma, epsilon)

def to_int(ar):
    return int(''.join([str(bit) for bit in ar]), 2)

print(to_int(gamma) * to_int(epsilon))

# 841526

# part 2

oxygen = set(lines)
co2 = set(lines)

def most_common(nums, bit):
    return int(sum([num[bit] for num in nums]) * 2 >= len(nums))

bit = 0
while len(oxygen) > 1:
    mc = most_common(oxygen, bit)
    oxygen = {num for num in oxygen if num[bit] == mc}
    bit += 1

oxygen = to_int(oxygen.pop())

bit = 0
while len(co2) > 1:
    mc = 1 - most_common(co2, bit)
    co2 = {num for num in co2 if num[bit] == mc}
    bit += 1

co2 = to_int(co2.pop())

print(co2 * oxygen)

# 4790390
