n = int(input())
a = list(map(int, input().split()))
a = [0] + a
dp = [[0] * (sum(a) + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(sum(a) + 1):
        if dp[i - 1][j] == 1:
            dp[i][j] = 1
            dp[i][j + a[i]] = 1
            if j > a[i]:
                dp[i][j - a[i]] = 1
print(sum(dp[n]) - 1)
