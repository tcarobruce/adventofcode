import sys
from collections import Counter


hands = [ln.strip().split() for ln in open(sys.argv[1])]

cards = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")
joker_cards = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")


def rank(hand_bid):
    hand, _ = hand_bid
    same_ranks = tuple(sorted(Counter(hand).values()))
    hand_types = [
        (5,), (1, 4), (2, 3), (1, 1, 3), (1, 2, 2), (1, 1, 1, 2), (1, 1, 1, 1, 1)
    ]
    return (hand_types.index(same_ranks), tuple([cards.index(c) for c in hand]))


def joker_rank(hand_bid):
    hand, _ = hand_bid
    counts = Counter(hand)
    jokers = counts.pop("J", 0)
    if counts:
        most_common = counts.most_common(1)[0][0]
    else:
        most_common = "A"  # all jokers!
    counts[most_common] += jokers
    same_ranks = tuple(sorted(counts.values()))
    hand_types = [
        (5,), (1, 4), (2, 3), (1, 1, 3), (1, 2, 2), (1, 1, 1, 2), (1, 1, 1, 1, 1)
    ]
    return (hand_types.index(same_ranks), tuple([joker_cards.index(c) for c in hand]))

# p1
hands.sort(key=rank, reverse=1)
print(sum([i * int(bid) for i, (hand, bid) in enumerate(hands, 1)]))

# p2
hands.sort(key=joker_rank, reverse=1)
print(sum([i * int(bid) for i, (hand, bid) in enumerate(hands, 1)]))
