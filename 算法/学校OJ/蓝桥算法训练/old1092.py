l, m = map(int, input().split())
a = [[0] * 2 for i in range(110)]
b = [0] * 10001
res = 0
for i in range(m):
    x, y = map(int, input().split())
    a[i][0], a[i][1] = x, y
for i in range(m):
    for j in range(a[i][0], a[i][1]+1):
        b[j] = 1
for i in range(l+1):
    if b[i] == 0:
        res += 1
print(res)
