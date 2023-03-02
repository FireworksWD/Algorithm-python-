v, n, t = map(int, input().split())
p = [0] * 11
w = [[0] * 11 for _ in range(1001)]
c = [[0] * 11 for _ in range(1001)]
dp = [0] * 20001
for i in range(1, n + 1):
    x, y, z = map(int, input().split())
    p[z] += 1
    w[z][p[z]] = x
    c[z][p[z]] = y
for i in range(1, t + 1):
    for j in range(v, -1, -1):
        for k in range(1, p[i]+1):
            if j >= w[i][k]:
                dp[j] = max(dp[j], dp[j - w[i][k]] + c[i][k])
print(dp[v])
