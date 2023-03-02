n, m = map(int, input().split())
bag = []
for i in range(n):
    bag.append(int(input()))
dp = [0] * (m + 1)
dp[0] = 1
for i in range(n):
    for j in range(bag[i], m + 1):
        dp[j] += dp[j - bag[i]]
print(dp[m])
