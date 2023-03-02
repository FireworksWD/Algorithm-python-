n = int(input())
ans = 0
vis = [False] * 10
res = [0] * 10
f = False


def dfs(temp):
    global ans
    global f
    if temp >= 10:
        ans += 1
        if ans == n:
            for i in res:
                print(i, end='')
            print()
            f = True
        return
    if f: return
    for i in range(10):
        if vis[i]: continue
        vis[i] = True
        res[temp] = i
        dfs(temp + 1)
        vis[i] = False


dfs(0)
