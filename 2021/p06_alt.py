# DP approach by @cs-cordero
import sys
from functools import lru_cache

initial = [int(n) for n in open(sys.argv[1]).read().strip().split(",")]

@lru_cache(maxsize=None)
def fish_after_days(days):
    if days <= 0:
        return 1
    return fish_after_days(days - 7) + fish_after_days(days - 9)

def count_fish(initial, days):
    return sum([fish_after_days(days - n) for n in initial])

print(count_fish(initial, 80))
print(count_fish(initial, 256))

# part 1: 386640
# part 2: 1733403626279
