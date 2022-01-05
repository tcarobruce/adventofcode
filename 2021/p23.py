from functools import lru_cache

part1_test = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########""".split("\n")

part1_real = """#############
#...........#
###B#A#B#C###
  #D#A#D#C#
  #########""".split("\n")

# part 1 by inspection
print(10 + 90 + 15000 + 1400 + 6)

part2_test = """#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########""".split("\n")

part2_real = """#############
#...........#
###B#A#B#C###
  #D#C#B#A#
  #D#B#A#C#
  #D#A#D#C#
  #########""".split("\n")

prob = part1_test

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

# datastructure = (hallway, siderooms)

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

def is_done(siderooms, amph):
    return all(siderooms[i] == amph for i in range(amph*depth, (amph+1)*depth))

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


def ph(hallway):
    for h in hallway:
        print("." if h is None else"ABCD"[h], end="")
    print()

def ps(siderooms):
    for offset in range(depth):
        print("##", end="")
        s = [siderooms[a * depth + offset] for a in range(4)]
        print("#".join("." if c is None else "ABCD"[c] for c in s), end="")
        print("##")


def _least_cost(hallway, siderooms):
    if siderooms == goal and hallway == gh:
        return 0

    dbg = 0
    if dbg:
        print('-' * 40)
        ph(hallway)
        ps(siderooms)

    moves = list(legal_moves(hallway, siderooms))
    moves.sort()

    for cost, move in moves:
        new_hallway, new_siderooms = make_move(hallway, siderooms, move)
        if dbg:
            print()
            ph(new_hallway)
            ps(new_siderooms)
            print(cost, move)
            # if not move[3]:
            #     input()
            input()
        new_cost = _least_cost(new_hallway, new_siderooms)
        if new_cost is not None:
            print("-" * 50)
            # ph(hallway)
            # ps(siderooms)
            print('->', cost, move )
            ph(new_hallway)
            ps(new_siderooms)
            return new_cost + cost


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
    x = sum(range(1, depth+1))
    base = sum([x * e for e in energy])  # cost of moving everyone back in
    print(base)
    return base + _least_cost(hallway, siderooms)

# ph(hallway)
# ps(siderooms)
# for lm in legal_moves(hallway, siderooms):
#     print(lm)
print(least_cost(hallway, siderooms))
