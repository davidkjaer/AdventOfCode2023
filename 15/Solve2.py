import re

def calculateHash(val: str) -> int:
    hash = 0
    for y in val:
        hash = ((hash + ord(y)) * 17) % 256
    return hash


with open("input.txt", "r") as input:
    codes = [x.strip() for x in input.readline().strip().split(",")]
    # parse string using regular expression "(\.)+(=|-)(\d)"
    # (\.)+ matches one or more dots
    # (=|-) matches either '=' or '-'
    # (\d) matches a digit
    hashMap = [[None for y in range(10)] for x in range(256)]
    focals = {}
    for x in codes:
        print(x)
        parsed = re.findall("(.+)(=|-)(\d*)", x)
        label, sign = parsed[0][0], parsed[0][1]
        if sign == "-":
            # remove label from hashMap
            hash = calculateHash(label)
            if label in hashMap[hash]:
                l = hashMap[hash]
                idx = l.index(label)
                l[idx] = None
                # Move all following elements forward
                for i in range(idx + 1, len(l)):
                    l[i - 1] = l[i]
                l[-1] = None
        else:
            # add label to hashMap
            hash = calculateHash(label)
            l = hashMap[hash]
            focal = int(parsed[0][2])
            focals[label] = focal
            if not label in l:
                # move focal to first vacant position
                pos = 0
                while l[pos]:
                    pos += 1
                l[pos] = label
    result = 0
    for i, x in enumerate(hashMap, 1):
        for j, y in enumerate(x, 1):
            if y:
                print(y, i, j, focals[y])
                result += i * j * focals[y]
    print(result)