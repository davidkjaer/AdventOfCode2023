import re
from collections import namedtuple

range = namedtuple("range", ["source", "target", "length"])

with open("input.txt", "r") as input:
    seed = input.readline().strip()
    seeds = [int(x.strip()) for x in seed.split(':')[1].strip().split(" ")]
    input.readline()
    # read lines until EOF
    
    tree = dict()
    valMap = dict()
    while True:
        line = input.readline().strip()
        if not line:
            break
        # Get source and target from string of format "source-to-target map:" using regex
        source, target = re.match(r"(.+)-to-(.+) map:", line).groups()
        while True:
            ranges = input.readline().strip()
            if not ranges:
                break
            ranges = ranges.strip()
            tree[source] = target
            ranges = [int(x.strip()) for x in ranges.strip().split(" ")]
            if not source in valMap:
                valMap[source] = []
            valMap[source].append(range(source=ranges[1], target=ranges[0], length=ranges[2]))

    # Now we have a tree and a map of values

    result = 1e9
    for seed in seeds:
        curVal = seed
        node = "seed"
        while node != "location":
            #print(f"Node: {node}, curVal: {curVal}")
            nextRange = next(filter(lambda x: x.source <= curVal and x.source + x.length > curVal, valMap[node]), None)
            nextVal = curVal
            #print(f"NextRange: {nextRange}")
            if nextRange:
                nextVal = nextRange.target + (curVal - nextRange.source)
            curVal = nextVal
            node = tree[node]
        
        #print(f"Node: {node}, curVal: {curVal}")
        result = min(result, curVal)
    print(result)




# Path: 6/Solve.py