import re
def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b % a, a)

with open("input.txt", "r") as file:
    directions = file.readline().strip()
    print(directions)
    file.readline()
    nodes = file.readlines()
    G = dict()
    for x in nodes:
        val, children = [y.strip() for y in x.split("=")]
        # parse childre from string (left, right) using regex
        components = re.findall(r"\((.+), (.+)\)", children)
        G[val] = (components[0][0], components[0][1])
    startElements = [x for x in G.keys() if x.endswith("A")]
    result = 1
    for x in startElements:
        nextStep = 0
        current = x
        curResult = 0
        while True:
            if current.endswith("Z"):
                break 
            curResult += 1
            current = G[current][0] if directions[nextStep] == "L" else G[current][1]
            nextStep = (nextStep + 1) % len(directions)
        result *= curResult // gcd(result, curResult)
    print(result)
