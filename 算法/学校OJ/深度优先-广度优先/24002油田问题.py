n, m = map(int, input().split())
grid = []
result = 0
dir = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
for i in range(n):
    grid.append(list(input()))


def check(x, y):
    if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == '@':
        return True
    return False


def dfs(x, y):
    grid[x][y] = '*'
    for i, j in dir:
        tx = x + i
        ty = y + j
        if check(tx, ty):
            dfs(tx, ty)
    return


for i in range(n):
    for j in range(m):
        if grid[i][j] == '@':
            result += 1
            dfs(i, j)
print(result)
