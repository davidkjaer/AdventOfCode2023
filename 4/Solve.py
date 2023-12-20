import re
from collections import Counter

with open("input.txt", "r") as file:
    result = 0
    for line in [x.strip() for x in file.readlines()]:
        card = line.split(":")
        game = card[1].strip().split("|")
        winning = Counter([int(num.strip()) for num in re.findall("\d+", game[0])])
        hasNumbers = Counter([int(num.strip()) for num in re.findall("\d+", game[1])])
        number = 0
        for x, val in winning.items():
            number += min(val, hasNumbers[x])

        if number > 0:
            result += 2 ** (number - 1)
    print(result)