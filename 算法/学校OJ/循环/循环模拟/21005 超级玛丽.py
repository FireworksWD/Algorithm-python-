n, m = map(int, input().split())
a = [0] * 105
b = [0] * 105
b[1] = 1
x = list(map(int, input().split()))
for j in x:
    a[j] += 1
for i in range(2, n + 1):
    if a[i]:
        b[i] = 0
    else:
        b[i] = b[i - 1] + b[i - 2]
print(b[n])
