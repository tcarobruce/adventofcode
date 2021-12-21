from itertools import cycle, count


def get_dice():
    return enumerate(cycle(range(1, 101)))

test = [4, 8]
prob = [10, 3]


def play(pos):
    scores = [0, 0]
    player = 0
    dice = get_dice()
    while True:
        pos[player] = (pos[player] + next(dice)[1] + next(dice)[1] +  next(dice)[1] - 1) % 10 + 1
        scores[player] += pos[player]
        if scores[player] >= 1000:
            return scores[1 - player] * next(dice)[0]
        #print(player, scores[player])
        player = 1 - player


print(play(test))
print(play(prob))




