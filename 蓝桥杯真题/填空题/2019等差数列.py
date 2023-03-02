import math

al = list(map(int, input().split()))
n = al[0]
a = al[1:]
a.sort()
d = 0
for i in range(1, n):
    d = math.gcd(d, a[i] - a[i - 1])
if not d:
    print(n)
else:
    print((a[n - 1] - a[0]) // d + 1)
