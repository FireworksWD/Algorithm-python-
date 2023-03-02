n, m = map(int, input().split())
value = list(map(int, input().split()))
price = list(map(int, input().split()))
dp = [0] * (m + 1)
for i in range(n):
    for j in range(m, price[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - price[i]] + value[i])
print(dp[m])
