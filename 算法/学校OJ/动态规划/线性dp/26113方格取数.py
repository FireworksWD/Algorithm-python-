al = list(map(int, input().split()))
n = al[0]
a = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(2, len(al), 3):
    a[al[i]][al[i + 1]] = al[i + 2]
dp = [[[[0 for _c in range(n + 1)] for _a in range(n + 1)] for _b in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            for l in range(1, n + 1):
                temp1 = max(dp[i - 1][j][k - 1][l], dp[i - 1][j][k][l - 1])
                temp2 = max(dp[i][j - 1][k - 1][l], dp[i][j - 1][k][l - 1])
                dp[i][j][k][l] = max(temp2, temp1) + a[i][j]
                if i != k and j != l:
                    dp[i][j][k][l] += a[k][l]
print(dp[n][n][n][n])
