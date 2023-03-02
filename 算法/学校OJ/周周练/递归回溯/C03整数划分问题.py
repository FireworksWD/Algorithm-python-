n, m = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i < j:
            dp[i][j] = dp[i][j]
        if i == j:
            dp[i][j] = dp[i][j - 1] + 1
        else:
            dp[i][j] = dp[i - j][j] + dp[i][j - 1]
print(dp[n][m])
