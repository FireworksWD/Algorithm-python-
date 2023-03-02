n, v = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (v + 1)
for i in range(n):
    for j in range(v, bag[i][0] - 1, -1):
        dp[j] = max(dp[j], dp[j - bag[i][0]] + bag[i][1])
print(dp[v])
