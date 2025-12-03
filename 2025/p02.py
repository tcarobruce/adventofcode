import sys
import math

ranges = []
invalid_sum = 0

def find_invalid_ids(range_):
    a, b = range_
    len_a = len(str(a))
    len_b = len(str(b))

    if len_a % 2 == 0:
        digits = len_a
        base = 10**(digits//2) + 1
        low = int(math.ceil(a / base)) * base
        high = min(b, 10**digits)
    elif len_b % 2 == 0:
        digits = len_b
        base = 10**(digits//2) + 1
        low = int(math.ceil(max(a, 10**(digits-1)) / base)) * base
        high = b
    else:
        return []

#    print("a %s ; b %s ; digits %s ; low %s ; high %s ; base %s" % (a, b, digits, low, high, base))

    for id in range(low, high + 1, base):
        yield id

for pair in open(sys.argv[1]).read().split(","):
    ranges.append(tuple([int(x) for x in pair.split("-")]))

for range_ in ranges:
    a, b = range_
    #print(len(str(a)), len(str(b)), len(str(b)) - len(str(a)))
    print(range_)
    for id in find_invalid_ids(range_):
        print("  ", id)
        invalid_sum += id
    #invalid_sum += sum(find_invalid_ids(range_))

print(invalid_sum)


