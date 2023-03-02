n, m = map(int, input().split())
a = [0] * 100001
f, i, s = 0, 0, 0
while True:
    i += 1
    if (n+1 == i):
        i = 1
    if (a[i] == 0):
        s += 1
    if (s == m):
        s = 0
        a[i] = 1
        f += 1
    if f == n:
        print(i)
        break
