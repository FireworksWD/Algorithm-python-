n = int(input())
nums = list(map(int, input().split()))
dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 0
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + nums[i - 1]
for k in range(2, n + 1):
    for l in range(1, n + 1):
        r = l + k - 1
        if r > n: continue
        for t in range(l, r):
            dp[l][r] = min(dp[l][t] + dp[t + 1][r] + s[r] - s[l - 1], dp[l][r])
print(dp[1][n])
