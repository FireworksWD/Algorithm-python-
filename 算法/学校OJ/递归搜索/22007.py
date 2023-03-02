m, n = map(int, input().split())
f = [[0] * 100 for _ in range(100)]
for j in range(1, m + 1):
    f[j][0] = 1
for j in range(m + 1):
    for i in range(j + 1, n + 1):
        f[j][i] = 0
for i in range(1, n + 1):
    for j in range(i, m + 1):
        f[j][i] = f[j - 1][i] + f[j][i - 1]
print(f[m][n])
