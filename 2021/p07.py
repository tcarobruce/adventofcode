import sys
from functools import lru_cache
positions = [int(c) for c in next(open(sys.argv[1])).strip().split(",")]

def fuel_cost(pos, positions):
    return sum([abs(pos - p) for p in positions])

# part 1: 352707
print(min(fuel_cost(p, positions) for p in range(min(positions), max(positions) + 1)))

# part 2: 95519693
@lru_cache(maxsize=None)
def step_cost(n):
    return int((n * (n + 1)) / 2)

def fuel_cost(pos, positions):
    return sum([step_cost(abs(pos - p)) for p in positions])

print(min(fuel_cost(p, positions) for p in range(min(positions), max(positions) + 1)))
