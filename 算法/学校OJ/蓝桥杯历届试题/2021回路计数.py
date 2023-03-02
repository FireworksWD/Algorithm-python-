# python 跑的相当慢，不过这是道填空题就无所谓了
import math

n = 1 << 21
dp = [[0] * (22) for i in range(n + 1)]
g = [[0 for i in range(22)] for i in range(22)]

for i in range(1, 22):
    for j in range(1, 22):
        if math.gcd(i, j) == 1:
            g[i - 1][j - 1] = g[j - 1][i - 1] = 1
dp[1][0] = 1
i = 1
while i < n:
    for j in range(0, 21):
        if (i >> j & 1) == 0:  # 当前所在的位置
            continue
        for k in range(0, 21):
            if g[j][k] == 0 or (i >> k & 1) != 0:  # 下一步可以去到的位置
                continue
            dp[(i + (1 << k))][k] += dp[i][j]
    i += 1
res = 0
for i in range(0, 21):
    res += dp[n - 1][i]
print(res)