import sys
from functools import lru_cache
from heapq import heappop, heappush
from random import random

# part 1 by inspection
print(10 + 90 + 15000 + 1400 + 6)

parts = ["""#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########""".split("\n"),
"""#############
#...........#
###B#A#B#C###
  #D#A#D#C#
  #########""".split("\n"),
"""#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########""".split("\n"),
"""#############
#...........#
###B#A#B#C###
  #D#C#B#A#
  #D#B#A#C#
  #D#A#D#C#
  #########""".split("\n"),
]

prob = parts[int(sys.argv[1]) - 1]

#0123456789A#
#...........#
###B#A#B#C###
  #D#C#B#A#
  #D#B#A#C#
  #D#A#D#C#

#0123456789A#
#...........#
###B#A#B#C###
  #D#C#B#A#
  #D#B#A#C#
  #D#A#D#C#


letters = "ABCD"
energy = [1, 10, 100, 1000]
entrances = [2, 4, 6, 8]
hallway = [None] * 11
siderooms = []

depth = len(prob) - 3
goal = [None] * 4 * depth
gh = [None] * 11
for c in [3, 5, 7, 9]:
    siderooms.extend([letters.index(ln[c]) for ln in prob[2:2+depth]])


def is_enterable(siderooms, amph):
    return all(siderooms[i] in {amph, None} for i in range(amph*depth, (amph+1)*depth))


def is_reachable(h1, h2, hallway):
    return all(hallway[i] is None for i in range(min(h1, h2), max(h1, h2) + 1))


def legal_moves(hallway, siderooms):
    for hallpos, amph in enumerate(hallway):
        if amph is None:
            continue
        if is_enterable(siderooms, amph):
            entrance = entrances[amph]
            if entrance > hallpos:
                hp = hallpos + 1
            else:
                hp = hallpos - 1
            if is_reachable(hp, entrance, hallway):
                cost = abs(entrance - hallpos) * energy[amph]
                yield cost, (amph, hallpos, None, False)
                return

    for sideroom in range(4):
        amph = None
        for d in range(depth):
            spot = depth * sideroom + d
            amph = siderooms[spot]
            if amph is not None:
                break
        if amph is None:
            continue
        for hallpos, other in enumerate(hallway):
            if other is not None or hallpos in entrances:
                continue
            if is_reachable(entrances[sideroom], hallpos, hallway):
                cost = (abs(hallpos - entrances[sideroom]) + d + 1) * energy[amph]
                yield cost, (amph, hallpos, spot, True)


def make_move(hallway, siderooms, move):
    amph, hallpos, spot, to_hall = move
    hallway = list(hallway)
    if to_hall:
        assert hallway[hallpos] is None
        assert siderooms[spot] == amph
        hallway[hallpos] = amph
        siderooms = list(siderooms)
        siderooms[spot] = None
    else:
        assert hallway[hallpos] == amph
        hallway[hallpos] = None
        # ignoring putting it back in siderooms, see base cost
    return hallway, siderooms


def pp(hallway, siderooms):
    for h in hallway:
        print("." if h is None else"ABCD"[h], end="")
    print()

    for offset in range(depth):
        print("##", end="")
        s = [siderooms[a * depth + offset] for a in range(4)]
        print("#".join("." if c is None else "ABCD"[c] for c in s), end="")
        print("##")


def _least_cost(hallway, siderooms):
    seen = set((tuple(hallway), tuple(siderooms)))

    states = [(0, 0, hallway, siderooms)]

    while True:
        cost, _, hallway, siderooms = heappop(states)
        th = tuple(hallway)
        ts = tuple(siderooms)
        if (th, ts) in seen:
            continue
        seen.add((th, ts))
        print(cost, len(states))
        if siderooms == goal and hallway == gh:
            return cost

        for new_cost, move in legal_moves(hallway, siderooms):
            new_hallway, new_siderooms = make_move(hallway, siderooms, move)
            n = (new_cost + cost, random(), new_hallway, new_siderooms)
            heappush(states, n)


def clean_siderooms(siderooms):
    s = []
    for amph in range(4):
        sideroom = []
        in_place = True
        for i in range(depth-1, -1, -1):
            a = siderooms[amph * depth + i]
            if a == amph and in_place:
                sideroom.insert(0, None)
            else:
                in_place = False
                sideroom.insert(0, a)
        s.extend(sideroom)
    return s

def least_cost(hallway, siderooms):
    siderooms = clean_siderooms(siderooms)

    base = 0  # cost to move back in
    for sideroom in range(4):
        for d in range(depth):
            if siderooms[sideroom * depth + d] is not None:
                base += energy[sideroom] * (d + 1)

    return base + _least_cost(hallway, siderooms)


print(least_cost(hallway, siderooms))
