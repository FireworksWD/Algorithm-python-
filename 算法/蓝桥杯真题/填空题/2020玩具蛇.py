cnt = 0
vis = [[0] * 17 for _ in range(17)]
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(index, x, y):
    global cnt
    if index == 16:
        cnt += 1
        return
    vis[x][y] = 1
    for xx, yy in dirs:
        tx, ty = x + xx, y + yy
        if tx >= 0 and tx < 4 and ty >= 0 and ty < 4 and vis[tx][ty] == 0:
            dfs(index + 1, tx, ty)
            vis[tx][ty] = 0


for i in range(4):
    for j in range(4):
        dfs(1, i, j)
        vis[i][j] = 0
print(cnt)
