with open("input.txt", "r") as input:
    extraval = 999999
    network = [x.strip() for x in input.readlines()]
    colPrefSum = [0 for x in range(len(network) + 1)]
    rowPrefSum = [0 for x in range(len(network[0]) + 1)]
    for i, x in enumerate(network, 1):
        rowPrefSum[i] = rowPrefSum[i - 1]
        if all(y == '.' for y in x):
            rowPrefSum[i] += extraval
    print(rowPrefSum)
    for x in range(1, len(network[0]) + 1):
        colPrefSum[x] = colPrefSum[x - 1]
        col = [y[x - 1] for y in network]
        if all(y == '.' for y in col):
            colPrefSum[x] += extraval
    print(colPrefSum)

    galaxies = [(x, y) for x in range(len(network)) for y in range(len(network[0])) if network[x][y] == '#']
    result = 0
    for i, x in enumerate(galaxies):
        for j in range(i, len(galaxies)):
            maxx, minx = max(galaxies[i][0], galaxies[j][0]), min(galaxies[i][0], galaxies[j][0])
            maxy, miny = max(galaxies[i][1], galaxies[j][1]), min(galaxies[i][1], galaxies[j][1])
            result += maxx - minx + maxy - miny + (rowPrefSum[maxx + 1] - rowPrefSum[minx]) + (colPrefSum[maxy + 1] - colPrefSum[miny])
    print(result)