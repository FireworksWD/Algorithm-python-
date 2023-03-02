a, b, c, d = [0] * 100005, [0] * 100005, [0] * 100005, [0] * 100005
x = list(map(int, input().split()))
n = x[0]
x.pop(0)
for i in range(n):
    a[i] = x[i]
c[0] = 1
for i in range(1,n):
    c[i] = c[i - 1] * a[i - 1]
d[n - 1] = 1
for i in range(n - 2, -1, -1):
    d[i] = d[i + 1] * a[i + 1]
for i in range(n):
    b[i] = c[i] * d[i]
    print(b[i], end=' ')
