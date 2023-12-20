import re
from math import sqrt, floor, ceil

with open("input.txt", "r") as input:
    timeStr = input.readline().strip().split(":")[1].strip()
    distanceStr = input.readline().strip().split(":")[1].strip()
    distances = [int(x.strip()) for x in re.findall(r"\d+", distanceStr)]
    times = [int(x.strip()) for x in re.findall(r"\d+", timeStr)]
    result = 1
    for record, time in zip(distances, times):
        # solve x * (time - x) - record = 0
        # x * time - x^2 - record = 0
        # x^2 - x * time + record = 0
        # x = (time +- sqrt(time^2 - 4 * record)) / 2
        discriminant = sqrt(time ** 2 - 4 * record)
        solutions = [(time - discriminant) / 2, (time + discriminant) / 2]
        #round down solutions[1] and round up solutions[0]
        roundedSolutions = [ceil(solutions[0]), floor(solutions[1])]
        if (roundedSolutions[0] == solutions[0]):
            roundedSolutions[0] += 1
        if (roundedSolutions[1] == solutions[1]):
            roundedSolutions[1] -= 1
        diff = min(time, roundedSolutions[1] - roundedSolutions[0] + 1)
        result *= min(time, diff)
    print(result)