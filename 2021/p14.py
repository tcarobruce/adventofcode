import sys
from collections import Counter
from functools import lru_cache

lines = [ln.strip() for ln in open(sys.argv[1])]

polymer = list(lines[0])

rules = dict(ln.split(' -> ') for ln in lines[2:])


@lru_cache(maxsize=None)
def counts(a, c, its):
    if its == 0:
        return Counter([a])  # don't double-count c
    b = rules[a + c]
    return counts(a, b, its-1) + counts(b, c, its-1)


def most_least_diff(polymer, iterations):
    mc = sum(
        [counts(a, b, iterations) for a, b in zip(polymer[:-1], polymer[1:])],
        Counter(polymer[-1]),  # count last letter
    ).most_common()
    return mc[0][1] - mc[-1][1]


# part 1: 2988
print(most_least_diff(polymer, 10))
# part 2: 3572761917024
print(most_least_diff(polymer, 40))
