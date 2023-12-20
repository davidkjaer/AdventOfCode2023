from typing import List
import copy
import time

# Rotate a matrix 90 degrees clockwise
def rotateRight(grid: List[List[str]]):
    N = len(grid)
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = grid[i][j]
            grid[i][j] = grid[N - 1 - j][i]
            grid[N - 1 - j][i] = grid[N - 1 - i][N - 1 - j]
            grid[N - 1 - i][N - 1 - j] = grid[j][N - 1 - i]
            grid[j][N - 1 - i] = temp

def moveRocksToTop(grid: List[List[str]]):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
                if grid[y][x] == "O":
                    for z in range(y, 0, -1):
                        if grid[z - 1][x] == "#" or grid[z - 1][x] == "O":
                            break
                        else:
                            # swap grid[z][x] and grid[z - 1][x]
                            temp = grid[z][x]
                            grid[z][x] = grid[z - 1][x]
                            grid[z - 1][x] = temp

# Move all rocks to its leftmost position in a line. Rocks are not moved if there is a rock or a '#' to its left.
def moveRocksLeft(grid: List[List[str]]):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O":
                for z in range(x, 0, -1):
                    if grid[y][z - 1] == "#" or grid[y][z - 1] == "O":
                        break
                    else:
                        # swap grid[y][z] and grid[y][z - 1]
                        temp = grid[y][z]
                        grid[y][z] = grid[y][z - 1]
                        grid[y][z - 1] = temp

# Move all rocks to its bottommost position in a line. Rocks are not moved if there is a rock or a '#' to below it.
def moveRocksDown(grid: List[List[str]]):
    for x in range(len(grid[0])):
        for y in range(len(grid) - 1, -1, -1):
            if grid[y][x] == "O":
                for z in range(y, len(grid) - 1):
                    if grid[z + 1][x] == "#" or grid[z + 1][x] == "O":
                        break
                    else:
                        # swap grid[z][x] and grid[z + 1][x]
                        temp = grid[z][x]
                        grid[z][x] = grid[z + 1][x]
                        grid[z + 1][x] = temp

# Move all rocks to its rightmost position in a line. Rocks are not moved if there is a rock or a '#' to its right.
def moveRocksRight(grid: List[List[str]]):
    for y in range(len(grid)):
        for x in range(len(grid[0]) - 1, -1, -1):
            if grid[y][x] == "O":
                for z in range(x, len(grid[0]) - 1):
                    if grid[y][z + 1] == "#" or grid[y][z + 1] == "O":
                        break
                    else:
                        # swap grid[y][z] and grid[y][z + 1]
                        temp = grid[y][z]
                        grid[y][z] = grid[y][z + 1]
                        grid[y][z + 1] = temp

def rowCounts(grid: List[List[str]]):
    return [sum(1 for x in y if x == "O") for y in grid]

with open("input.txt") as input:
    G = [list(x.strip()) for x in input.readlines()]
    N = len(G)
    print(N, len(G[0]))
    hasSeen = dict()
    round = 1
    while True:
        print(round)
        moveRocksToTop(G)
        moveRocksLeft(G)
        moveRocksDown(G)
        moveRocksRight(G)
        key = tuple(map(tuple, G))
        if key in hasSeen.keys():
            cycle = round - hasSeen[key]
            break
        else:
            hasSeen[tuple(map(tuple, G))] = round
        round += 1
    left = (1000000000 - round) % cycle
    print("Left: ", left)
    while left > 0:
        moveRocksToTop(G)
        moveRocksLeft(G)
        moveRocksDown(G)
        moveRocksRight(G)
        left -= 1
    
    result = 0
    for x in range(len(G[0])):
        for y in range(len(G)):
            if G[y][x] == "O":
                result += N - y
    print(result)