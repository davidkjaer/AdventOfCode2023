from typing import List
import logging
import re

logger = logging.getLogger(__name__)

def getNext(sequence: List[int]) -> int:
    logger.debug(sequence) 
    if all(x == 0 for x in sequence):
        return 0
    nextSequence = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
    nextLast = getNext(nextSequence)
    return nextLast + sequence[-1]


def getFirst(sequence: List[int]) -> int:
    logger.debug(sequence) 
    if all(x == 0 for x in sequence):
        return 0
    nextSequence = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
    nextFirst = getFirst(nextSequence)
    return sequence[0] - nextFirst

with open("input.txt", "r") as input:
    nextResult = 0
    prevResult = 0
    for line in input.readlines():
        if line.strip() == "":
            break
        sequence = [int(x.strip()) for x in line.strip().split(" ")]
        if len(sequence) == 0:
            break
        nextResult += getNext(sequence)
        prevResult += getFirst(sequence)
    print(prevResult)