from collections import deque

dirdelta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
GDeltas = {'/': [3, 2, 1, 0], '\\': [1, 0, 3, 2]}
G = []

def can(x: int, y: int, dir: int) -> bool:
    return x >= 0 and x < len(G) and y >= 0 and y < len(G[0]) and not vis[x][y][dir]

def bfs(x: int, y: int, dir: int):
    if vis[x][y][dir]:
        return
    vis[x][y][dir] = True

    q = deque()
    def movenext(ndir: int):
        nx = x + dirdelta[ndir][0]
        ny = y + dirdelta[ndir][1]
        if can(nx, ny, ndir):
            q.append((nx, ny, ndir))

    q.append((x, y, dir))
    while len(q) > 0:
        x, y, dir = q.popleft()
        vis[x][y][dir] = True
        if G[x][y] == ".":
            movenext(dir)
        if G[x][y] == "/":
            ndir = GDeltas["/"][dir]
            movenext(ndir)
        if G[x][y] == "\\":
            ndir = GDeltas["\\"][dir]
            movenext(ndir)
        if G[x][y] == "-":
            if dir == 1 or dir == 3:
                movenext((dir + 1) % 4)
                movenext((dir + 3) % 4)
            else:
                movenext(dir)
        elif G[x][y] == '|':
            if dir == 0 or dir == 2:
                movenext((dir + 1) % 4)
                movenext((dir + 3) % 4)
            else:
                movenext(dir)

with open("input.txt", "r") as input:
    G = [x.strip() for x in input.readlines()]
    startPos = []
    for x in range(len(G[0])):
        startPos.append((x, 0, 0))
    for x in range(len(G[0])):
        startPos.append((len(G) - 1, x, 3))
    for x in range(len(G)):
        startPos.append((x, len(G[0]) - 1, 2))
    for x in range(len(G[0])):
        startPos.append((0, x, 1))
    result = 0
    for pos in startPos:
        vis = [[[False for x in range(4)] for z in range(len(G[0]))] for y in range(len(G))]
        startx, starty, startdir = pos
        bfs(startx, starty, startdir)
        curResult = 0
        for x in range(len(G)):
            for y in range(len(G[0])):
                if any(vis[x][y]):
                    curResult += 1
        result = max(result, curResult)
    print(result)