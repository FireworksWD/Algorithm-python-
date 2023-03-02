n = int(input())
a = [0] * (10 ** 5 + 1)
b = [0] * (10 ** 6 + 1)
res = [0] * (10 ** 6 + 1)
for i in range(1, n + 1):
    x = int(input())
    a[i] = x
    b[a[i]] += 1
for i in range(1, n + 1):
    j = 1
    while j * j <= a[i]:
        if a[i] % j == 0:
            res[i] += b[j]
        if a[i] % (a[i] // j) == 0 and a[i] // j != j:
            res[i] += b[a[i] // j]
        j += 1
for i in range(1, n + 1):
    print(res[i] - 1)
