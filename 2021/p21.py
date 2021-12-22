from itertools import cycle, count, product
from collections import Counter, defaultdict
from functools import lru_cache


def get_dice():
    return enumerate(cycle(range(1, 101)))

test = [4, 8]
prob = [10, 3]


def add_pos(a, b):
    pos = a + b
    while pos > 10:
        pos -= 10
    return pos


def play(pos):
    pos = list(pos)  # copy
    scores = [0, 0]
    player = 0
    dice = get_dice()
    while True:
        for _ in range(3):
            pos[player] = add_pos(pos[player], next(dice)[1])
        scores[player] += pos[player]
        if scores[player] >= 1000:
            return scores[1 - player] * next(dice)[0]
        #print(player, scores[player])
        player = 1 - player


print(play(test))
print(play(prob))


rolls = list(Counter([sum(p) for p in product([1, 2, 3], repeat=3)]).items())
# [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]

# scores maps score -> position -> ways to get to this score + position
def turn(scores):
    # yield the updated "scores" data structure, and count of wins / no wins
    new_scores = defaultdict(Counter)
    wins = no_wins = 0
    for score, positions in scores.items():
        for (pos, ways), (roll, roll_ways) in product(positions.items(), rolls):
            pos = add_pos(pos, roll)
            new_score = score + pos
            new_ways = ways * roll_ways
            if new_score >= 21:
                wins += new_ways
            else:
                no_wins += new_ways
                new_scores[score + pos][pos] += new_ways
    return new_scores, wins, no_wins


def quantum(pos):
    scores = {0: {pos: 1}}
    while True:
        scores, wins, no_wins = turn(scores)
        yield wins, no_wins
        if no_wins == 0:
            break


def most_winning(starting_positions):
    possibilities = [list(quantum(start)) for start in starting_positions]
    total_wins = [0, 0]

    for t in range(1, max(len(possibilities[0]), len(possibilities[1]))):
        total_wins[0] += possibilities[0][t][0] * possibilities[1][t - 1][1]
        # t instead of t-1 because player 1 goes first and can win on their turn
        total_wins[1] += possibilities[1][t][0] * possibilities[0][t][1]

    return max(total_wins)


print(most_winning(test))
print(most_winning(prob))
