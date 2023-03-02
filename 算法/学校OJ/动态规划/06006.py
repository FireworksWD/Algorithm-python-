m, n = map(int, input().split())
bag = []
for i in range(n):
    bag.append(list(map(int, input().split())))
dp = [0] * (m + 1)
for i in range(n):
    for j in range(bag[i][0], m + 1):
        dp[j] = max(dp[j], dp[j - bag[i][0]] + bag[i][1])
print(dp[-1])
