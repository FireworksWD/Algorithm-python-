n, m = map(int, input().split())
a = [0] * 1000005
a[0] = 0
a[1] = 2
res = 0
for i in range(2, n + 1):
    if i % 2 == 0:
        a[i] = a[i - 1] + 7
    else:
        a[i] = a[i - 1] + 8
res = a[n]
for i in range(n + 1, m + 1):
    if i % 2 == 0:
        a[i] = a[i - 1] + 7
    else:
        a[i] = a[i - 1] + 8
    res += a[i]
print(res)
