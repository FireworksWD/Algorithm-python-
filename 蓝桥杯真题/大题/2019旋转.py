m, n = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
dp = [[0] * m for _ in range(n)]
for i in range(m):
    for j in range(n):
        dp[j][m - i - 1] = a[i][j]
for i in dp:
    print(*i)
