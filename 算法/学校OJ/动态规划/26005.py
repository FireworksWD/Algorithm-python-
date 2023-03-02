n, m = map(int, input().split())
bag = []
for i in range(m):
    x, y = map(int, input().split())
    bag.append([x, x * y])
dp = [0] * (n + 1)
for i in range(m):
    for j in range(n, bag[i][0] - 1, -1):
        dp[j] = max(dp[j], dp[j - bag[i][0]] + bag[i][1])
print(dp[-1])
