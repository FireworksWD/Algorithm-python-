al = list(map(int, input().split()))
n = al[0]
a = al[1:]
dpmax = [0] * n
dpmin = [0] * n
for i in range(n):
    dpmax[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            dpmax[i] = max(dpmax[i], dpmax[j] + 1)
for i in range(n):
    dpmin[i] = 1
    for j in range(i):
        if a[j] >= a[i]:
            dpmin[i] = max(dpmin[i], dpmin[j] + 1)
print(max(dpmin), max(dpmax))
