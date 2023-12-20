def calculateHash(val: str) -> int:
    hash = 0
    for y in val:
        hash = ((hash + ord(y)) * 17) % 256
    return hash


with open("input.txt", "r") as input:
    codes = [x.strip() for x in input.readline().strip().split(",")]
    print(sum(calculateHash(x) for x in codes))