from typing import List, Optional

def findMirror(grid: List[str]) -> Optional[int]:
    print(grid)
    for i, x in enumerate(grid[:-1]):
        diff = 0
        for j in range(i + 1):
            if i + j + 1== len(grid):
                break
            if diff > 1:
                break
            # count number of different characters in zip(grid[i - j], grid[i + j + 1])
            diff += sum(1 for x in zip(grid[i - j], grid[i + j + 1]) if x[0] != x[1])
        if diff == 1:
            print(i + 1)
            return i + 1
    return None

def transpose(grid:List[str]) -> List[str]:
    return ["".join([x[y] for x in grid]) for y in range(len(grid[0]))]

with open("input.txt", "r") as input:
    result = 0
    while True:
        grid = []
        while True:
            line = input.readline().strip()
            print(line)
            if line == "":
                break
            grid.append(line)
        if len(grid) == 0:
            break
        rowM = findMirror(grid)
        if rowM:
            result += 100 * rowM
        else:
            colM = findMirror(transpose(grid))
            if colM:
                result += colM

    print(result)