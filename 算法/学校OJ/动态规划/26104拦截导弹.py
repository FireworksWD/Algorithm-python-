a1 = list(map(int, input().split()))
n = a1[0]
a = a1[1:]
dp = [0] * n
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
