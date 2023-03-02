gra = [[0] * 101 for _ in range(101)]
best_v = float('inf')
vis = [0] * 101
path = [0] * 101
n, m = map(int, input().split())
for i in range(m):
    u, v, w = map(int, input().split())
    gra[u][v] = w
    gra[v][u] = w


def dfs(k, temp):
    global best_v
    if best_v < temp:
        return
    if k > n:
        temp += gra[path[k]][1]
        best_v = temp
        return
    else:
        for j in range(1, n + 1):
            if vis[j]: continue
            vis[j] += 1
            path[k] = j
            dfs(k + 1, temp + gra[path[k]][j])
            vis[j] -= 1
            path[k] = 0


dfs(1, 0)
print(best_v)
