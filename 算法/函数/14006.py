n = int(input())
a = [True] * n
b = []
res = []
for i in range(2, n):
    if a[i]:
        b.append(i)
    for k in b:
        l = k * i
        if l >= n:
            break
        a[l] = False
        if k % i == 0:
            break
for i in b:
    if i >= n // 2 + 1:
        break
    if (n - i) in b and (n - i) != i:
        res.append((n - i) * i)
print(max(res))
