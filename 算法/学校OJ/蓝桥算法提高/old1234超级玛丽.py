n, m = map(int, input().split())
a1 = list(map(int, input().split()))
dp = [0] * 41
b = [0] * 41
dp[1] = 1
for i in range(m):
    b[a1[i]] += 1
for i in range(2, n + 1):
    if b[i]:
        dp[i] = 0
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])
