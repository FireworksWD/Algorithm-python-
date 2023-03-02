n, m = map(int, input().split())
board = []
ans = 0
for i in range(n):
    board.append(list(input()))
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def check(x, y):
    if x >= 0 and x < n and y >= 0 and y < m and board[x][y] != '0':
        return True
    return False


def dfs(x, y):
    board[x][y] = '0'
    for i, j in dir:
        tx = x + i
        ty = y + j
        if check(tx, ty):
            dfs(tx, ty)


for i in range(n):
    for j in range(m):
        if board[i][j] != '0':
            ans += 1
            dfs(i, j)
print(ans)
