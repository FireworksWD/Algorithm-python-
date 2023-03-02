def dfs(x, y):
    max_hight = 1
    if dp[x][y] > 0:
        return dp[x][y]
    for k in range(4):
        tx = x + next_[k][0]
        ty = y + next_[k][1]
        if tx < 0 or tx >= r or ty < 0 or ty >= c:
            continue
        if arr[tx][ty] >= arr[x][y]:
            continue
        max_hight = max(max_hight, dfs(tx, ty) + 1)
    dp[x][y] = max_hight
    return dp[x][y]
r, c = map(int, input().split())
dp = [[0 for _ in range(c)]for _ in range(r)]
arr = [list(map(int, input().split()))for _ in range(r)]
next_ = [[0, 1], [1, 0], [0, -1], [-1, 0]]
ans = 0
for i in range(r):
    for j in range(c):
        ans = max(ans, dfs(i, j))
print(ans)