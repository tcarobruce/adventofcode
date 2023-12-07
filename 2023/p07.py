import sys
from collections import Counter


hands = [ln.strip().split() for ln in open(sys.argv[1])]

cards = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")

card_rank = cards.index


def rank(hand_bid):
    hand, _ = hand_bid
    same_ranks = tuple(sorted(Counter(hand).values()))
    hand_types = [
        (5,), (1, 4), (2, 3), (1, 1, 3), (1, 2, 2), (1, 1, 1, 2), (1, 1, 1, 1, 1)
    ]
    return (hand_types.index(same_ranks), tuple([card_rank(c) for c in hand]))

hands.sort(key=rank, reverse=1)
print(sum([i * int(bid) for i, (hand, bid) in enumerate(hands, 1)]))
