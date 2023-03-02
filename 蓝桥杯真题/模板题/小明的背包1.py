n, v = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
dp = [0] * (v + 1)
for i in range(n):
    for j in range(v, a[i][0] - 1, -1):
        dp[j] = max(dp[j], dp[j - a[i][0]] + a[i][1])
print(dp[-1])
