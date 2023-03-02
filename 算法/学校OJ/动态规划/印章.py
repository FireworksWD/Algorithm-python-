n, m = map(int, input().split())
dp=[[0.00000000000000000 ]*25 for j in range(25)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if i < j:
            dp[i][j] = 0
        elif j == 1:
            dp[i][j] = (1 / n) ** (i - 1)
        else:
            dp[i][j] = (dp[i - 1][j]) * (j * 1.0 / n) + (dp[i - 1][j - 1]) * ((n - j + 1) * 1.0 / n)  # 状态转移函数

s = float(dp[m][n])
print("%.4f" % s)