n, m = map(int, input().split())
bag = []
for i in range(m):
    v, x = map(int, input().split())
    bag.append([v, v * x])
dp = [0] * (n + 1)
for i in range(m):
    for j in range(n, bag[i][0] - 1, -1):
        dp[j] = max(dp[j], dp[j - bag[i][0]] + bag[i][1])
print(dp[n])
