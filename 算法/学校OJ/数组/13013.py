a = list(map(int, input().split()))
n = a[0]
a.pop(0)
s = [0] * 1000001
s[0] = a[0] ** 2
for i in range(1, n):
    s[i] = s[i - 1] + a[i] ** 2
max_n = s[0] * sum(a[2:n])
for i in range(1, n):
    t = s[i] * sum(a[i + 1:n])
    if t > max_n:
        max_n = t
print(max_n)
