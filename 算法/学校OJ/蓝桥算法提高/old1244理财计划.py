a, b, c = map(str, input().split())
k, n, p = int(a), int(b), float(c)
res = ans = 0
for i in range(1, n + 1):
    res += k
    res *= (1 + p)
print('%.2f' % (res - n * k))
