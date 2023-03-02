n, m = map(int, input().split())
res = [0] * (n + 2)
for i in range(m):
    r, l, c = map(int, input().split())
    res[r] += c
    res[l + 1] -= c
for i in range(1, n + 1):
    res[i] += res[i - 1]
    print(res[i], end=' ')
