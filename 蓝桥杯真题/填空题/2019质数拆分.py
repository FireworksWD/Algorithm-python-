a = [True] * 2020
res = []
for i in range(2, 2020):
    if a[i]: res.append(i)
    for j in res:
        if i * j >= 2020:
            break
        a[i * j] = False
        if i % j == 0:
            break
dp = [0] * 2020
dp[0] = 1
for i in range(len(res)):
    for j in range(2019, res[i] - 1, -1):
        dp[j] += dp[j - res[i]]
print(dp[2019])
