import re
from collections import Counter
from functools import cache

with open("input.txt", "r") as file:
    result = 0
    cards = []

    @cache
    def calculate(at: int) -> int:
        winnings = cards[at]
        result = 1
        for x in range(at + 1, at + winnings + 1):
            result += calculate(x)
        return result

    for line in [x.strip() for x in file.readlines()]:
        card = line.split(":")
        game = card[1].strip().split("|")
        winning = Counter([int(num.strip()) for num in re.findall("\d+", game[0])])
        hasNumbers = Counter([int(num.strip()) for num in re.findall("\d+", game[1])])
        number = 0
        for x, val in winning.items():
            number += min(val, hasNumbers[x])
        cards.append(number)
    
    result = sum([calculate(x) for x in range(len(cards))])
    print(result)