vis = [False] * 10
res = []
s = [str(i) for i in range(10)]
f = False


def dfs(k):
    global f
    if k == 10:
        # print(res)
        t = int(''.join(res))
        if int(t ** 0.5) == t ** 0.5:
            print(t)
            f = True
    if f: return
    for i in reversed(range(10)):
        if vis[i]: continue
        vis[i] = True
        res.append(s[i])
        dfs(k + 1)
        vis[i] = False
        res.pop()


dfs(0)
