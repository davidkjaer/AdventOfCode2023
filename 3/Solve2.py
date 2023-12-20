from typing import Optional

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    def getNumber(line, idx):
        if idx < 0 or idx + 1 >= len(line) or not line[idx].isdigit():
            return None
        startIdx, endIdx = idx, idx + 1
        while startIdx >= 0 and line[startIdx].isdigit():
            startIdx -= 1
        while endIdx < len(line) and line[endIdx].isdigit():
            endIdx += 1
        return int(line[startIdx + 1:endIdx])
    def addIfValid(number: Optional[int], numbers: list):
        if number:
            numbers.append(number)

    result = 0
    for i, x in enumerate(lines):
        for j, val in enumerate(x):
            if val == '*':
                numbers = []
                if i > 0:
                    num = getNumber(lines[i - 1], j)
                    if num:
                        addIfValid(num, numbers)
                    else:
                        addIfValid(getNumber(lines[i - 1], j - 1), numbers)
                        addIfValid(getNumber(lines[i - 1], j + 1), numbers)
                addIfValid(getNumber(x, j - 1), numbers)
                addIfValid(getNumber(x, j + 1), numbers)
                if i + 1 < len(lines):
                    num = getNumber(lines[i + 1], j)
                    if num:
                        addIfValid(num, numbers)
                    else:
                        addIfValid(getNumber(lines[i + 1], j - 1), numbers)
                        addIfValid(getNumber(lines[i + 1], j + 1), numbers)
                if len(numbers) == 2:
                    result += numbers[0] * numbers[1]
    print(result)