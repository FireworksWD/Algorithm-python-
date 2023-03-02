n = int(input())
dpmin = [[float('inf')] * 301 for _a in range(301)]
dpmax = [[float('-inf')] * 301 for _b in range(301)]
sums = [0] * 301
b = [0] + list(map(int, input().split()))
a = [0] * 301
for i in range(1, n + 1):
    a[i] = b[i]
    a[i + n] = a[i]
for i in range(1, 2 * n + 1):
    sums[i] = sums[i - 1] + a[i]
    dpmax[i][i] = 0
    dpmin[i][i] = 0
minn, maxx = float('inf'), float('-inf')
for le in range(2, n + 1):
    for i in range(1, n * 2 - le + 1 + 1):
        j = le + i - 1
        for k in range(i, j):
            dpmin[i][j] = min(dpmin[i][j], dpmin[i][k] + dpmin[k + 1][j] + sums[j] - sums[i - 1])
            dpmax[i][j] = max(dpmax[i][j], dpmax[i][k] + dpmax[k + 1][j] + sums[j] - sums[i - 1])
for i in range(1, n + 1):
    minn = min(minn, dpmin[i][i + n - 1])
    maxx = max(maxx, dpmax[i][i + n - 1])
print(minn)
print(maxx)
