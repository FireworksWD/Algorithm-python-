x = list(map(int, input().split()))
n, m = x[0], x[1]
le = x[2:]
if sum(le) < m:
    print(-1)
else:
    l, r = 0, 1000000
    while l < r:
        mid = (l + r + 1) // 2
        ct = 0
        for i in range(n):
            ct += le[i] // mid
        if ct < m:
            r = mid - 1
        else:
            l = mid
    print(r)
