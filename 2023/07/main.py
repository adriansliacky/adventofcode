from collections import Counter
from functools import cmp_to_key as c2k

with open('input.txt') as file:
    data = file.read().strip().splitlines()


def hand_type(counts):
    hand_types = {
        5: 1,  # 'High Card'
        4: 2,  # 'One Pair'
        3: 3 if counts[0] == 2 else 4,  # 'Two Pair' or 'Three of a Kind'
        2: 5 if counts[0] == 3 else 6,  # 'Full House' or 'Four of a Kind'
        1: 7  # 'Five of a Kind'
    }
    return hand_types[len(counts)]


def hand_strength(hand, wild_card):
    if not wild_card or 'J' not in hand:
        return hand_type(sorted(Counter(hand).values(), reverse=True))
    else:
        return max(
            hand_type(sorted(Counter([val if v == 'J' else v for v in hand]).values(), reverse=True)) for val in VALUES)


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

VALUES = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
print(calculate_total(CARDS_BIDS, True))
