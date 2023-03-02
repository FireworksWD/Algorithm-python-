n = int(input())
a = [True] * (n + 1)
res = []
for i in range(2, n + 1):
    if a[i]:
        res.append(i)
    for j in res:
        l = j * i
        if l >= n + 1:
            break
        a[l] = False
        if i % j == 0:
            break
i = 0
j = len(res) - 1
ans = 0
while i <= j:
    if res[i] + res[j] <= n:
        ans = ans + j - i + 1
        i += 1
    else:
        j -= 1
print(ans)
