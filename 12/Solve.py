from functools import cache

groups = []
springs = ""

@cache
def dp(at: int, grp: int, left: int, inGrp: bool) -> int:
    if at == len(springs):
        return 1 if (grp + 1 == len(groups) and left == 0) else 0
    if left < 0:
        return 0
    if springs[at] == ".":
        if inGrp:
            if left > 0:
                return 0
            nxtGrp = grp + 1 if grp + 1 < len(groups) else grp
            nxtLeft = groups[nxtGrp] if grp + 1 < len(groups) and inGrp else 0
            return dp(at + 1, nxtGrp, nxtLeft, False)
        return dp(at + 1, grp, left, False)
    if springs[at] == '#':
        return dp(at + 1, grp, left - 1, True)
    if inGrp:
        if left == 0:
            if grp + 1 < len(groups): 
                return dp(at + 1, grp + 1, groups[grp + 1], False)
            else:
                return dp(at + 1, grp, 0, False)
        else:
            return dp(at + 1, grp, left - 1, True)
    else:
        return dp(at + 1, grp, left - 1, True) + dp(at + 1, grp, left, False)

with open("input.txt", "r") as input:
    result = 0
    for line in input.readlines():
        dp.cache_clear()
        splitLine = line.strip().split(" ")
        springs = splitLine[0]
        #repeat springs 5 times
        springs = "?".join([springs] * 5)
        groups = [int(x.strip()) for x in splitLine[1].split(",")] * 5
        curResult = dp(0, 0, groups[0], False)
        print(springs, groups)
        print(curResult)
        result += curResult
    print("Final result:", result)