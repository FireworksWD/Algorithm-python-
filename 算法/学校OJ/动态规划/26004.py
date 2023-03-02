t, m = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(m)]
dp = [0] * (t + 1)
for i in range(m):
    for j in range(t, bag[i][0] - 1, -1):
        dp[j] = max(dp[j], dp[j - bag[i][0]] + bag[i][1])
print(dp[-1])
