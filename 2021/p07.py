import sys
positions = [int(c) for c in next(open(sys.argv[1])).strip().split(",")]

def fuel_cost(pos, positions):
    return sum([abs(pos - p) for p in positions])

# part 1: 352707
print(min(fuel_cost(p, positions) for p in range(min(positions), max(positions) + 1)))
