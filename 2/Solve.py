import re
from collections import Counter
colCounts = Counter({'red': 12, 'green' : 13, 'blue' : 14})

def isValid(ball: str) -> bool:
    number, color = re.findall(r'\d+|\D+', ball)
    return int(number) <= colCounts[color.strip()]

with open("test.txt", "r") as input:
    result = 0
    for line in [line.strip() for line in input.readlines()]:
        game = line.split(':')
        # fetch game id "Game 1" using regular expression
        gameId = int(re.findall(r'\d+', game[0])[0])
        can = True
        for round in [x.strip() for x in game[1].split(';')]:
            can = all(isValid(ball) for ball in [ball.strip() for ball in round.split(',')])
            if not can:
                break
        result += int(gameId) if can else 0
    print(result)
