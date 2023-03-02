s = [list(input()) for _ in range(10)]
vis = [[0] * 10 for i in range(10)]
ans = 0


def dfs(x, y):
    global ans
    if x > 9 or y > 9 or x < 0 or y < 0:
        ans += 1
        return
    if vis[x][y] == 1:
        return
    vis[x][y] = 1
    if s[x][y] == 'U':
        dfs(x - 1, y)
    if s[x][y] == 'D':
        dfs(x + 1, y)
    if s[x][y] == 'L':
        dfs(x, y - 1)
    if s[x][y] == 'R':
        dfs(x, y + 1)


for i in range(10):
    for j in range(10):
        vis = [[0] * 10 for i in range(10)]
        dfs(i, j)
print(ans)
