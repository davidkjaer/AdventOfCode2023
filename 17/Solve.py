import numpy as np
from sortedcontainers import SortedSet

with open("input.txt") as input:
    G = [x.strip() for x in input.readlines()]
    dist = np.zeros((len(G), len(G[0]), 10, 4))
    dist.fill(1e9)
    q = SortedSet()
    for i in range(4):
        dist[0][0][0][i] = 0
        q.add((0, (0, 0, 0, i)))
    dirdelta  = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def relax(oldDist, x, y, num, dir):
        if x < 0 or x >= len(G) or y < 0 or y >= len(G[0]) or num >= 10:
            return
        if oldDist + int(G[x][y]) < dist[x][y][num][dir]:
            q.discard((dist[x][y][num][dir], (x, y, num, dir)))
            dist[x][y][num][dir] = oldDist + int(G[x][y])
            q.add((dist[x][y][num][dir], (x, y, num, dir)))
    while q:
        distance, (x, y, num, dir)  = q.pop(0)
        if dist[x][y][num][dir] < distance:
            continue
        relax(distance, x + dirdelta[dir][0], y + dirdelta[dir][1], num + 1, dir)
        if num >= 3:
            ndir = (dir + 1) % 4
            relax(distance, x + dirdelta[ndir][0], y + dirdelta[ndir][1], 0, ndir)
            ndir = (dir + 3) % 4
            relax(distance, x + dirdelta[ndir][0], y + dirdelta[ndir][1], 0, ndir)
    result = 1e9
    for i in range(4, 10):
        for j in range(4):
            result = min(result, dist[len(G) - 1][len(G[0]) - 1][i][j])
    print(int(result))