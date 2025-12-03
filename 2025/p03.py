import sys

total = 0

def max_joltage(bank):
    if len(bank) < 2:
        return 0
    return max(10 * bank[0] + max(bank[1:]), max_joltage(bank[1:]))

for ln in open(sys.argv[1]):
    bank = [int(c) for c in ln.strip()]
    m = max_joltage(bank)
    print(ln, m)
    total += m

print(total)
