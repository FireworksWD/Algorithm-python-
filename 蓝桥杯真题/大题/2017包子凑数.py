import math

num = 10000
# n = int(input())
# S = list(int(input()) for i in range(n))
al = list(map(int, input().split()))
n = al[0]
S = al[1:]
t = S[0]
dp = [0] * num
dp[0] = 1
for i in range(n):
    t = math.gcd(t, S[i])
if t != 1:
    print('INF')
else:
    for i in S:
        for j in range(i, num):
            if i == j:
                dp[j] = 1
            else:
                dp[j] = max(dp[j - i], dp[j])
    print(num - sum(dp))
