import math
from functools import cmp_to_key

data = open("./data.txt").read().splitlines()
hands = [x.split() for x in data]

card_strength = ["T", "Q", "K", "A"]


def get_hand_type(hand):
    # 6 is the best and 0 the worst
    occurences, jokers = {}, 0
    for x in hand: 
        if x == "J":
            jokers += 1
            continue
        if x in occurences: occurences[x] += 1
        else: occurences[x] = 1
    occ_sorted = sorted(list(occurences.values()))
    if len(occ_sorted) == 0: occ_sorted.append(0)
    occ_sorted[-1] += jokers
    if len(occ_sorted) == 1: return 6
    if len(occ_sorted) == 2 and occ_sorted[0] in [1, 4]: return 5
    if len(occ_sorted) == 2: return 4
    if occ_sorted[-1] == 3: return 3
    if occ_sorted[-2:] == [2, 2]: return 2
    if occ_sorted[-1] == 2: return 1
    return 0

def get_card_strength(card):
    if card.isdigit(): return int(card)
    if card == "J": return 1
    return card_strength.index(card) +  10

def compare_hands(a, b):
    a, b = a[0], b[0]
    type_dif = get_hand_type(a) - get_hand_type(b)
    if type_dif != 0: return type_dif
    for x, y in zip(a, b):
        x, y = get_card_strength(x), get_card_strength(y)
        if x - y != 0: return x - y

sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))
ans = sum(int(x[1]) * (i + 1) for i, x in enumerate(sorted_hands))
print(ans)
