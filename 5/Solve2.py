import re
from collections import namedtuple
from collections import deque

rangePair = namedtuple("rangePair", ["source", "target", "length"])

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
            valMap[source].append(rangePair(source=ranges[1], target=ranges[0], length=ranges[2]))

    # Now we have a tree and a map of values

    result = 1e9
    #print(seeds)
    for seed in range(0, len(seeds), 2):
        curRanges = deque()
        curRanges.append((seeds[seed], seeds[seed + 1]))
        #print(curRanges)
        node = "seed"
        while node != "location":
            #print(f"Node: {node}, curVal: {curVal}")
            nextRanges = deque()
            #print(node, curRanges)
            while curRanges:
                rangeSource, rangeLen = curRanges.popleft()
                nextRange = next(filter(lambda x: x.source <= rangeSource and x.source + x.length > rangeSource, valMap[node]), None)
                if nextRange:
                    nextVal = nextRange.target + (rangeSource - nextRange.source)
                    nextEnd = min(nextRange.target + nextRange.length, nextVal + rangeLen)
                    hasUsed = nextEnd - nextVal
                    nextLength = min(nextRange.length, hasUsed)
                    if hasUsed < rangeLen:
                        curRanges.append((rangeSource + hasUsed, rangeLen - hasUsed))
                    nextRanges.append((nextVal, nextLength))
                else:
                    endpoint = rangeSource + rangeLen
                    # Find range that intersects on endpoint
                    nextRange = next(filter(lambda x: x.source > rangeSource and x.source < endpoint, valMap[node]), None)
                    if nextRange:
                        nextVal = nextRange.target
                        nextLength = min(nextRange.length, rangeLen - (nextRange.source - rangeSource))
                        nextRanges.append((nextVal, nextLength))
                        curRanges.append((rangeSource,  nextRange.source - rangeSource))
                        if endpoint > nextRange.source + nextRange.length:
                            curRanges.append((endpoint, endpoint - (nextRange.source - nextRange.length)))
                    else:
                        nextRanges.append((rangeSource, rangeLen))
            curRanges = nextRanges
            node = tree[node]
       # print(node, curRanges)
       # print("\n")
        #print(f"Node: {node}, curVal: {curVal}")
        # get the minimum source in all ranges
        result = min(result, min([x[0] for x in curRanges]))
    print(result)




# Path: 6/Solve.py