import sys
from itertools import product

txt = open(sys.argv[1]).read().split("\n\n")
schemas = [s.strip().split() for s in txt]

keys, locks = [], []
for s in schemas:
    heights = [sum([c == "#" for c in col]) - 1 for col in zip(*s)]
    [keys, locks][s[0] == "#####"].append(heights)

def fit(key, lock):
    return all(a + b <= 5 for a, b in zip(key, lock))

print(sum([fit(key, lock) for key, lock in product(keys, locks)]))

