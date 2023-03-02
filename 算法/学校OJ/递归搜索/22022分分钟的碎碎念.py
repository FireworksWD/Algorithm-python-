al = list(map(int, input().split()))
n = al[0]
ans = 0
dp = [0] * (n + 1)
for i in range(1, n+1):
    dp[i] = dp[al[i]] + 1
    ans = max(dp[i], ans)
print(ans)
