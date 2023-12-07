import collections
from functools import cmp_to_key as c2k

with open('input.txt') as file:
    data = file.read().strip().splitlines()


def hand_type(counts):
    if len(counts) == 5:
        return 1  # 'High Card'
    elif len(counts) == 4:
        return 2  # 'One Pair'
    elif len(counts) == 3:
        if counts[0] == 2:
            return 3  # 'Two Pair'
        else:
            return 4  # 'Three of a Kind'
    elif len(counts) == 2:
        if counts[0] == 3:
            return 5  # 'Full House'
        else:
            return 6  # 'Four of a Kind'
    else:
        return 7  # 'Five of a Kind'


def hand_strength(hand, wild_card):
    counts = sorted(collections.Counter(hand).values(), reverse=True)
    if not wild_card or 'J' not in hand:
        return hand_type(counts)
    else:
        return max(
            hand_type(sorted(collections.Counter([value if v == 'J' else v for v in hand]).values(), reverse=True)) for
            value in VALUES)


def compare(a, b, wild_card):
    a_type, b_type = hand_strength(a, wild_card), hand_strength(b, wild_card)
    if a_type != b_type:
        return a_type - b_type
    else:
        return next((VALUES.index(b[i]) - VALUES.index(a[i])) for i in range(5) if a[i] != b[i])


def calculate_total(cards, wild_card):
    cards = sorted(cards, key=lambda x: (c2k(lambda a, b: compare(a, b, wild_card))(x[0]), x[0]))
    return sum(int(cards[i][1]) * (i + 1) for i in range(len(cards)))


CARDS_BIDS = [line.split() for line in data]
VALUES = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

print(calculate_total(CARDS_BIDS, False))

VALUES.pop(3)
VALUES.append('J')
print(calculate_total(CARDS_BIDS, True))
