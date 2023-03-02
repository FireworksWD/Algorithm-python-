l, m = map(int, input().split())
vis = [0] * 10001
for i in range(m):
    x, y = map(int, input().split())
    for j in range(x, y + 1):
        vis[j] += 1
ans = 0
for i in range(0, l+1):
    if vis[i]: continue
    ans += 1
print(ans)
