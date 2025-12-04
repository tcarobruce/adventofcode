import sys
import math

ranges = []

invalid_sum = invalid_sum2 = 0

def is_invalid(n, max_reps=None):
    digits = len(str(n))
    for zeros in range(0, digits // 2):
        div, mod = divmod(digits, (zeros + 1))
        if mod != 0:
            continue
        if max_reps is not None and div > max_reps:
            continue
        sub = ('0' * zeros + '1')
        d = int('1' + sub * (div - 1))
        #print(zeros, sub, d, n % d)
        if n % d == 0:
            return True
    return False

for pair in open(sys.argv[1]).read().split(","):
    a, b = [int(x) for x in pair.split("-")]

    print(a, b)
    for n in range(a, b + 1):
        if is_invalid(n, 2):
            #print(' ', n)
            invalid_sum += n
        if is_invalid(n):
            #print(' ', n)
            invalid_sum2 += n

print(invalid_sum)
print(invalid_sum2)


