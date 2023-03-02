s = [i for i in range(1, 14)]
ans = 0
vis = [False] * 14


def dfs(k, path: list):
    global ans
    if k == 13:
        if path[10] == path[11] * path[12]:
            ans += 1
        return
    if k == 3 and path[0] + path[1] != path[2]: return
    if k == 6 and path[3] - path[4] != path[5]: return
    if k == 9 and path[6] * path[7] != path[8]: return
    for i in range(13):
        if vis[i]: continue
        vis[i] = True
        path.append(s[i])
        dfs(k + 1, path)
        vis[i] = False
        path.pop()


dfs(0, [])
print(ans)
