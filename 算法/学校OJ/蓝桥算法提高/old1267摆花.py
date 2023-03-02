n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + a
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(m + 1):
        temp = min(a[i], j)
        for k in range(temp + 1):
            dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % 1000007
print(dp[n][m] % 1000007)