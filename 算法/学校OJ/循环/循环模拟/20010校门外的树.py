l, m = map(int, input().split())
a = []
ans = 0
for i in range(m):
    s = list(map(int, input().split()))
    a.append(s)
b = [0] * 10001
a.insert(0, [0, 0])
for i in range(1, m + 1):
    for j in range(a[i][0], a[i][1] + 1):
        b[j] = 1
for k in range(l+1):
    if b[k] == 0:
        ans += 1
print(ans)
