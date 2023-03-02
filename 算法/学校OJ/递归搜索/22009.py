a = list(map(int, input().split()))
n, t = a[0], a[1]
a.pop(0)
dp = [0] * 10000
dp[0] = 1
for i in range(1, n + 1):
    for j in range(t, a[i] - 1, -1):
        dp[j] += dp[j - a[i]]
if dp[t] > 0:
    print(1)
else:
    print(0)
print(dp)