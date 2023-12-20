from collections import Counter, namedtuple
from functools import cmp_to_key

def getType(hand: str):
    counts = Counter(hand)
    jokers = counts["J"]
    counts["J"] = 0
    # find the item in the hand that has the most occurences
    sortedCounts = max(counts.items(), key=lambda x: x[1])
    counts[sortedCounts[0]] += jokers 

    values = [x for x in counts.values()]
    if max(values) == 5:
        return 1
    if max(values) == 4:
        return 2
    if max(values) == 3:
        if 2 in values:
            return 3
        return 4
    if values.count(2) == 2:
        return 5
    if values.count(2) == 1:
        return 6
    return 7

cardOrder = "J23456789TJQKA"

with open("input.txt", "r") as input:
    hand = namedtuple("hand", ["hand", "bid"])
    def compare(h1: hand, h2: hand):
        if getType(h1.hand) == getType(h2.hand):
            for x in zip(h1.hand, h2.hand):
                if x[0] != x[1]:
                    return cardOrder.index(x[0]) - cardOrder.index(x[1])
        return getType(h2.hand) - getType(h1.hand)
    
    lines = [x.strip() for x in input.readlines()]
    hands = [hand(x, int(y)) for (x,y) in [line.split(" ") for line in lines]]
    # sort hands by type then by card order
    sortedHands = sorted(hands, key=cmp_to_key(compare))
    #     #sortedHands = sorted(hands, key=lambda x: (getType(x.hand), hand.hand))
    print(sortedHands )
    result = 0
    for i, hand in enumerate(sortedHands):
        result += hand.bid * (i + 1)
    print(result)