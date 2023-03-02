al = list(map(int, input().split()))
n, m = al[0], al[1]
G = [[0] * 201 for i in range(201)]
for i in range(2, len(al), 2):
    u, v = al[i], al[i + 1]
    G[u][v] = 1
    G[v][u] = 1
vis = [0] * (n + 1)
ans, temp = 0, 0
res = []


def dfs(t):
    global ans, temp, res
    if t > n:
        if ans < temp:
            ans = temp
            res = vis[:]
        return
    ok = 1
    for i in range(t):
        if vis[i] == 1 and G[t][i] == 1:
            ok = 0
            break
    if ok:
        vis[t] = 1
        temp += 1
        dfs(t + 1)
        temp -= 1
        vis[t] = 0
    if temp + n - t > ans:
        vis[t] = 0
        dfs(t + 1)


dfs(1)
print(ans, end=' ')
for i in range(1, n + 1):
    print(res[i], end=' ')
