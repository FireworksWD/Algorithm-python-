n = int(input())
a = [True] * (n + 1)
b = []
ans = 0
for i in range(2, n + 1):
    if a[i]:
        b.append(i)
    for j in b:
        l = i * j
        if l >= n + 1:
            break
        a[l] = False
        if i % j == 0:
            break
for i in range(len(b)):
    for j in range(i + 1, len(b)):
        k = n - b[i] - b[j]
        if k <= b[i] or k <= b[j]:
            break
        if k in b and k != b[i] and k != b[j]:
            ans += 1
print(ans)