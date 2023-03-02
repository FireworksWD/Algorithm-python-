n, m = 30, 50
path = [[''] * m for _a in range(n)]
vis = [[0] * m for _b in range(n)]
gra = [[int(i) for i in input()] for _c in range(n)]
dirs = [[1, 0, 'D'], [0, -1, 'L'], [0, 1, 'R'], [-1, 0, 'U']]
q, vis[0][0] = [], 1
q.append([0, 0])
while q:
    x, y = q.pop(0)
    if x == n - 1 and y == m - 1:
        print(path[n-1][m-1])
        break
    for xx, yy, dis in dirs:
        tx = xx + x
        ty = yy + y
        if tx >= 0 and tx < n and ty >= 0 and ty < m and gra[tx][ty] == 0 and vis[tx][ty] == 0:
            vis[tx][ty] = 1
            q.append([tx, ty])
            path[tx][ty] = path[x][y] + dis
