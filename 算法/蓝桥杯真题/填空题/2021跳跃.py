direct = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (3, 0)]
n, m = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(n)]
# dp = [[float('-inf')] * (m + 3) for _b in range(n + 3)]
# for i in range(3, n + 3):
#     for j in range(3, m + 3):
#         if i == 3 and j == 3:
#             dp[i][j] = gra[i - 3][j - 3]
#         else:
#             dp[i][j] = gra[i - 3][j - 3] + max(dp[i - 1][j], dp[i - 2][j], dp[i - 3][j], dp[i - 1][j - 1],
#                                                dp[i - 1][j - 2], dp[i - 2][j - 1], dp[i - 2][j - 2], dp[i][j - 1],
#                                                dp[i][j - 2], dp[i][j - 3])
# print(dp[-1][-1])
ans, w = float('-inf'), gra[0][0]


def dfs(x, y):
    global ans, w
    if x == n - 1 and y == m - 1:
        ans = max(ans, w)
        return
    for xx, yy in direct:
        tx = xx + x
        ty = yy + y
        if tx >= 0 and tx < n and ty >= 0 and ty < m:
            w += gra[tx][ty]
            dfs(tx, ty)
            w -= gra[tx][ty]


dfs(0, 0)
print(ans)
