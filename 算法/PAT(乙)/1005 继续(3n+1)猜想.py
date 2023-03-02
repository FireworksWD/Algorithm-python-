n = int(input())
a = list(map(int, input().split()))
vis = [False] * 101
for i in a:
    if not vis[i]:
        j = i
        while j != 1:
            if j & 1:
                j = (j * 3 + 1) >> 1
                vis[j] = True
            else:
                j >>= 1
                vis[j] = True
res = []
for i in a:
    if not vis[i]:
        res.append(i)
print(*sorted(res, reverse=True))
