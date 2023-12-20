with open("input.txt") as input:
    G = [x.strip() for x in input.readlines()]
    result = 0
    N = len(G)
    M = len(G[0])
    for x in range(M):
        curStop = 0
        for y in range(N):
            if G[y][x] == "#":
                curStop = y + 1
            elif G[y][x] == "O":
                result += N - curStop
                curStop += 1
    print(result)