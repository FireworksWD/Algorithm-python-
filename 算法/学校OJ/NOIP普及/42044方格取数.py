n, m = map(int, input().split())
b=[list(map(int,input().split())) for _ in range(n)]
a = [[0] * 1010 for _ in range(1010)]
for i in range(1, 1 + n):
    for j in range(1, 1 + m):
        a[i][j] = b[i-1][j-1]
dp = [[[float('-inf')] * 2] * 1010] * 1010
dp[1][0][0] = 0
for j in range(1, 1+m):
    for i in range(1, 1+n):
        dp[i][j][0] = max(dp[i][j - 1][0], dp[i][j - 1][1], dp[i - 1][j][0]) + a[i][j]
    for i in range(n, 0, -1):
        dp[i][j][0] = max(dp[i][j - 1][0], dp[i][j - 1][1], dp[i + 1][j][1]) + a[i][j]
print(dp[n][m][0])
