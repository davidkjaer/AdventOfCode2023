import re
from collections import Counter
from functools import reduce

colCounts = Counter({'red': 12, 'green' : 13, 'blue' : 14})

def isValid(ball: str) -> bool:
    return int(number) <= colCounts[color.strip()]

with open("input.txt", "r") as input:
    result = 0
    for line in [line.strip() for line in input.readlines()]:
        game = line.split(':')
        # fetch game id "Game 1" using regular expression
        colors = {'red' : 0, 'green' : 0, 'blue' : 0}
        for round in [x.strip() for x in game[1].split(';')]:
            for ball in [ball.strip() for ball in round.split(',')]:
                number, color = re.findall(r'\d+|\D+', ball)
                old = colors[color.strip()]
                colors[color.strip()] = max(old, int(number))
        result += reduce(lambda x, y: x * y, colors.values(),1)
    print(result)
