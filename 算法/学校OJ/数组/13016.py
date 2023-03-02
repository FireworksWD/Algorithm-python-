a = [0] * 200010
res = 0
x = list(map(int, input().split()))
n = x[0]
for i in range(1, n + 1):
    a[100000 + x[i]] += 1
for i in range(0, 200001):
    if a[i] != 0:
        res += 1
if a[100000] != 0:
    res -= 1
print(res)
