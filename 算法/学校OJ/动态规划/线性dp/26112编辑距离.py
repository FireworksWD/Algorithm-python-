a = input()
b = input()
m, n = len(a), len(b)
dp = [[0] * 201 for _ in range(201)]
for i in range(m + 1):
    dp[i][0] = i
for i in range(n + 1):
    dp[0][i] = i
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
print(dp[m][n])
