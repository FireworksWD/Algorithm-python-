al = list(map(int, input().split()))
n = al[0]
a = al[1:]
f, g = [0] * n, [0] * n
res = 1
for i in range(n):
    f[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            f[i] = max(f[i], f[j] + 1)
for i in range(n - 1, -1, -1):
    g[i] = 1
    for j in range(n - 1, i, -1):
        if a[j] < a[i]:
            g[i] = max(g[i], g[j] + 1)
for i in range(n):
    res = max(res, f[i] + g[i] - 1)
print(res)
