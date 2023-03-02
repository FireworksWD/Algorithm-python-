n, m = map(int, input().split())
res = 0
for i in range(m):
    l, r, s, e = map(int, input().split())
    res += (r - l + 1) * (s + e) // 2
print(res)
