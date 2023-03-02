import math

n = int(input())
a = list(map(int, input().split()))
a.sort()
d = 0
for i in range(1, n):
    d = math.gcd(d, a[i] - a[i - 1])
if d == 0:
    print(n)
else:
    print((a[n-1] - a[0]) // d + 1)
