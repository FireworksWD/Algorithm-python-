n, k = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)
s = [0] * 100005
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]
ans = 0
st = 0
for i in range(1, n + 1):
    if s[i] - s[st] < k and st == 0:
        continue
    ans += st
    for j in range(0, i + 1):
        if s[i] - s[st] >= k:
            ans += 1
        else:
            break
print(ans)
