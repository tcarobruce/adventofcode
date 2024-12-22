import sys
from util import Vec as V, readints
from collections import Counter

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


def evolvemanyseqs(n, many=2000):
    seq = []
    last = n % 10
    for _ in range(many):
        n = evolve(n)
        price = n % 10
        if len(seq) < 4:
            seq.append(price - last)
        else:
            seq = seq[1:] + [price - last]
            yield tuple(seq), price
        last = price


seq_prices = Counter()

for s in starts:
    seen = set()
    for seq, price in evolvemanyseqs(s):
        if seq in seen:
            continue
        seen.add(seq)
        seq_prices[seq] += price


# print(seq_prices)
print(max(seq_prices.values()))
