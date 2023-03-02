al = list(map(int, input().split()))
n, k = al[0], al[1]
dp = [0] * k
dp[0], p, ans = 1, [0], 0
a = al[2:]
for i in range(n):
    p.append(p[-1] + a[i])
for i in range(n):
    m = p[i + 1] % k
    ans += dp[m]
    dp[m] += 1
print(ans)
