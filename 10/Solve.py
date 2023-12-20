from queue import Queue
from typing import List, Tuple
from logging import Logger
import numpy

logger = Logger(__name__)

vis = set()
G = []
dist = dict()

def getNext(val: str) -> List[Tuple[int, int]]:
    steps = {'-': [(0, 1), (0, -1)],
     '|': [(1, 0), (-1, 0)],
     'L': [(-1, 0), (0, 1)],
     'J': [(0, -1), (-1, 0)],
     '7': [(0, -1), (1, 0)],
     'F': [(0, 1), (1, 0)],
     #'S': [(1, 0), (0, 1)]}
     'S': [(0, -1), (-1, 0)]}
    return steps[val]


def isValid(x: int, y: int) -> bool:
    return x >= 0 and x < len(G) and y >= 0 and y < len(G[0]) and G[x][y] != '.'


def bfs(x: int, y: int) -> int:
    logger.debug(f"bfs({x}, {y})")
    q = Queue()
    q.put((x, y))
    while not q.empty():
        curx, cury = q.get()
        logger.debug(f"visiting ({curx}, {cury})")
        vis.add((curx, cury))
        for dx in getNext(G[curx][cury]):
            nextx, nexty = curx + dx[0], cury + dx[1]
            if not isValid(nextx, nexty) or (nextx, nexty) in vis:
                continue
            dist[(nextx, nexty)] = dist[(curx, cury)] + 1
            q.put((nextx, nexty))
    return 0

with open("input.txt", "r") as input:
    G = [x.strip() for x in input.readlines()]
    for x in range(len(G)):
        for y in range(len(G[0])):
            if G[x][y] == 'S':
                dist[(x, y)] = 0
                bfs(x, y)
    #print(G)
    #print(dist)
    vals = [[0 for x in range(len(G[0]))] for y in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G[0])):
           if (i,j) in dist:
               vals[i][j] = 1
 
    print(max(dist.values()))
    # part 2
    def findOnes(nums: List[int]):
        try:
            first = nums.index(1)
        except ValueError:
            return (-1, -1)
        last = len(nums) - 1 - nums[::-1].index(1)
        return (first, last)
    for x in vals:
        print("".join([str(y) for y in x]))

    for i, x in enumerate(vals):
        # get index of first and last 1 in x
        first, last = findOnes(x)
        if first == -1:
            continue
        ones = 0
        for j in range(first, last):
            if vals[i][j] == 1:
                ones += 1
            if vals[i][j] != 1 and ones % 2 == 1:
                vals[i][j] = 2
    for x in vals:
        print("".join([str(y) for y in x]))

    result = 0
    for i in range(len(G[0])):
        first, last = findOnes([vals[x][i] for x in range(len(G))])
        if first == -1:
            continue
        ones = 0
        for j in range(first, last):
            if vals[j][i] == 1:
                ones += 1

            if vals[j][i] == 2 and ones % 2 == 1:
                result += 1

    print(result)