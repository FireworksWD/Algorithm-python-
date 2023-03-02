v = int(input())
n = int(input())
bag = []
res = v
for i in range(n):
    bag.append(int(input()))
dp = [v] * (v + 1)
for i in range(n):
    for j in range(v, bag[i] - 1, -1):
        dp[j] = min(dp[j], dp[j - bag[i]] - bag[i])
print(dp[v])
