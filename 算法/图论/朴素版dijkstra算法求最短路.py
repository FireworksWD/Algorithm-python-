'''给定一个n个点m条边的有向图，图中可能存在重边和自环，所有边权均为正值。
请你求出1号点到n号点的最短距离，如果无法从1号点走到n号点，则输出-1。
输入格式
第一行包含整数n和m。
接下来m行每行包含三个整数x，y，z，表示存在一条从点x到点y的有向边，边长为z。
输出格式
输出一个整数，表示1号点到n号点的最短距离。
如果路径不存在，则输出-1。
输入：
3 3
1 2 2
2 3 1
1 3 4
输出：
3
'''
n, m = map(int, input().split())
adj = [[float('inf')] * (n + 1) for _ in range(n + 1)]
dist = [float('inf')] * (n + 1)


def dijstra():
    global n
    st = [False] * (n + 1)
    dist[1] = 0
    for i in range(n):
        t = -1
        for j in range(1, n + 1):
            if not st[j] and (t == -1 or dist[j] < dist[t]): t = j  # 找到离0点最近的未访问过的点
        if t == -1: return
        st[t] = True
        for j in range(1, n + 1):
            dist[j] = min(dist[j], adj[t][j] + dist[t])  # 用t作为中间点，更新所有t能到的点


for _ in range(m):
    a, b, w = map(int, input().split())
    if a == b: continue
    adj[a][b] = min(adj[a][b], w)

dijstra()
if dist[n] == float('inf'):
    print(-1)
else:
    print(dist[n])