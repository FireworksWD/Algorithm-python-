vis = [False] * 10
res = []
ans = 0


def dfs(k):
    global ans
    if k == 9:
        if int(res[0]) + (res[1] / res[2]) + (res[3] * 100 + res[4] * 10 + res[5]) / (
                res[6] * 100 + res[7] * 10 + res[8]) == 10:
            ans += 1
        return
    for i in range(1, 10):
        if not vis[i]:
            vis[i] = True
            res.append(i)
            dfs(k + 1)
            vis[i] = False
            res.pop()


dfs(0)
print(ans)
