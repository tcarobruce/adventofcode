import sys

lines = open(sys.argv[1]).read().splitlines()


def to_dec(sn):
    d = {"-": -1, "=": -2}
    n = 0
    for c in sn:
        n *= 5
        n += int(d.get(c, c))
    return n

def to_snafu(n):
    s = ""
    while n:
        n, rem = divmod(n, 5)
        if rem == 3:
            n += 1
            rem = "="
        elif rem == 4:
            n += 1
            rem = "-"
        s = str(rem) + s
    return s


print(to_snafu(sum([to_dec(l) for l in lines])))
# 2---0-1-2=0=22=2-011

