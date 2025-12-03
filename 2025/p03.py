import sys
from functools import cache

p1 = p2 = 0
banks = []

@cache
def max_joltage(bank_id, switches, idx=0):
    if switches == 0:
        return 0
    bank = banks[bank_id]
    if len(bank) - idx < switches:
        return 0
    a = 10**(switches-1) * bank[idx] + max_joltage(bank_id, switches-1, idx=idx+1)
    b = max_joltage(bank_id, switches, idx=idx+1)
    return max(a, b)

for i, ln in enumerate(open(sys.argv[1])):
    bank = [int(c) for c in ln.strip()]
    banks.append(bank)
    m1 = max_joltage(i, 2)
    m2 = max_joltage(i, 12)
    # print(i, ln, m1, m2)
    p1 += m1
    p2 += m2

print(p1)
print(p2)
