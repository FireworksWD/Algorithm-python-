a1 = list((map(int, input().split())))
m, n = a1[0], a1[1]
bag = a1[2:]
dp = [0] * (m + 1)
dp[0] = 1
for i in range(n):
    for j in range(m, bag[i] - 1, -1):
        dp[j] += dp[j - bag[i]]
print(dp[m])
