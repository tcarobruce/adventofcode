import sys
from util import readints
from math import prod

def smush(ints):
    return int("".join([str(i) for i in ints]))

lines = [ln.strip() for ln in open(sys.argv[1])]
races = list(zip(readints(lines[0]), readints(lines[1])))

def count_wins(duration, record_distance):
    wins = 0
    for pressed in range(duration):
        if pressed * (duration - pressed) > record_distance:
            wins += 1
    return wins

print(
    prod(count_wins(duration, record_distance)
    for duration, record_distance in races)
)
print(count_wins(smush(readints(lines[0])), smush(readints(lines[1]))))
