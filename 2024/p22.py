import sys
from util import Vec as V, readints

f = open(sys.argv[1])
starts = [int(s.strip()) for s in f]


def evolve(n):
    n = (n ^ (n * 64)) % 16777216
    n = (n ^ (n // 32)) % 16777216
    n = (n ^ (n * 2048)) % 16777216
    return n

def evolvemany(n, many=2000):
    for _ in range(many):
        n = evolve(n)
    return n


print(sum([evolvemany(n) for n in starts]))
