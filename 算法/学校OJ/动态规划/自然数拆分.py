n = int(input())
dp = [[0] * 4050 for _ in range(4050)]
s = 0
while n:
    dp[0][0] = 1
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            dp[i][k] = dp[i - 1][k - 1] + dp[i - k][k]
    for k in range(1, n + 1):
        s += dp[n][k]
    print((s - 1) % 100000)
    break
