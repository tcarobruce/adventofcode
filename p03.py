import sys

lines = [
    [int(i) for i in ln.strip()] for ln in open(sys.argv[1])
]

# part 1
totals = lines[0]

for i, ln in enumerate(lines, 1):
    for j, x in enumerate(ln):
        totals[j] += x

gamma, epsilon = [], []

half = i / 2
for bit in totals:
    gamma.append(int(bit > half))
    epsilon.append(int(bit < half))

print(gamma, epsilon)

def to_int(ar):
    return int(''.join([str(bit) for bit in ar]), 2)

print(to_int(gamma) * to_int(epsilon))


