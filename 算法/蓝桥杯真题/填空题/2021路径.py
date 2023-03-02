import math


def gbs(x, y):
    return x * y // math.gcd(x, y)


dp = [float('inf')] * 2022
dp[1] = 0
for i in range(1, 2022):
    for j in range(i + 1, i + 22):
        if j > 2021: break
        dp[j] = min(dp[j], gbs(i, j) + dp[i])
print(dp[2021])
