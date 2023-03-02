n, k = map(int, input().split())
dp = [0 for i in range(k)]
dp[0] = 1  # 第一次当余数为0时是倍数
ans = 0
p = [0]
for i in range(n):
    tep = int(input())
    p.append(p[-1] + tep)
    m = p[i + 1] % k
    ans += dp[m]
    dp[m] += 1

print(ans)
