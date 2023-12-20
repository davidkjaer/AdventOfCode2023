with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    inNumber = False
    hasSymbol = False
    result = 0
    def isSymbol(c: str) -> bool:
        print("Checking", c)
        return c != '.' and not c.isdigit()
    for i, x in enumerate(lines):
        curNumber = 0
        canUse = False
        for j, val in enumerate(x):
            hasSymbol = isSymbol(val) or (i > 0 and isSymbol(lines[i - 1][j])) or ( i + 1 < len(lines) and isSymbol(lines[i + 1][j]))
            print(i, j, hasSymbol, canUse, inNumber, curNumber, val)
            if val.isdigit():
                if inNumber:
                    curNumber = curNumber * 10 + int(val)
                else:
                    inNumber = True
                    curNumber = int(val)
                canUse = canUse or hasSymbol
            else:
                if inNumber:
                    inNumber = False
                    if canUse or hasSymbol:
                        print("Adding", curNumber)
                        result += curNumber
            if not inNumber:
                canUse = hasSymbol
        if inNumber:
            if canUse or hasSymbol:
                result += curNumber
    print(result)
