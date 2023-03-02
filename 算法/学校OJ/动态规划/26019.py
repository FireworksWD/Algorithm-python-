import math

n = int(input())
a = []
dp = [0] * 101
dp[0] = 1
res = 0
for i in range(n):
    a.append(int(input()))
g = 0
for i in range(n):
    g = math.gcd(g, a[i])
if g != 1:
    print(-1)
else:
    for i in range(n):
        for j in range(a[i], 101):
            dp[j] += dp[j - a[i]]
    for i in range(101):
        if dp[j] > 0:
            res += 1
    print(res)
