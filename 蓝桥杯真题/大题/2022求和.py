n = int(input())
a = list(map(int, input().split()))
res = []
res.append(a[0])
for i in range(1, n):
    res.append(res[-1] + a[i])
ans = 0
for i in range(n-1):
    ans += (a[i] * (res[-1] - res[i]))
print(ans)
