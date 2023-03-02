n, m = map(int, input().split())
gra = [[int(i) for i in input()] for _a in range(n)]
vis = [[0] * m for _b in range(n)]
path = [[''] * m for _c in range(n)]
dirs = [[1, 0, 'D'], [0, -1, 'L'], [0, 1, 'R'], [-1, 0, 'U']]
distance = [[0] * m for _d in range(n)]
q, vis[0][0] = [[0, 0]], 1
while q:
    x, y = q.pop(0)
    if x == n - 1 and y == m - 1:
        print(distance[-1][-1])
        print(path[-1][-1])
        break
    for xx, yy, dis in dirs:
        tx, ty = xx + x, yy + y
        if tx >= 0 and tx < n and ty >= 0 and ty < m and gra[tx][ty] == 0 and vis[tx][ty] == 0:
            vis[tx][ty] = 1
            q.append([tx, ty])
            path[tx][ty] = path[x][y] + dis
            distance[tx][ty] = distance[x][y] + 1
