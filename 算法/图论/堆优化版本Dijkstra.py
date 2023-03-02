'''给定一个n个点m条边的有向图，图中可能存在重边和自环，所有边权均为非负值。
请你求出1号点到n号点的最短距离，如果无法从1号点走到n号点，则输出-1。
输入格式
第一行包含整数n和m。
接下来m行每行包含三个整数x，y，z，表示存在一条从点x到点y的有向边，边长为z。
输出格式
输出一个整数，表示1号点到n号点的最短距离。
如果路径不存在，则输出-1。
数据范围
1≤n,m≤1.5×10^5
图中涉及边长均不小于0，且不超过10000。
输入：
3 3
1 2 2
2 3 1
1 3 4
输出：
3
'''
from heapq import *

n, m = map(int, input().split())
idx = 0
h = [-1] * (n + 1)
e, ne, w = [0] * (2 * m + 1), [0] * (2 * m + 1), [0] * (2 * m + 1)
st, dist = [False] * (n + 1), [float('inf')] * (n + 1)


def add(a, b, wei):
    global idx
    e[idx], w[idx] = b, wei
    h[a], ne[idx] = idx, h[a]
    idx += 1


def dijkstra():
    heap = []
    heappush(heap, [0, 1])
    dist[1] = 0
    while heap:
        d, cur_idx = heappop(heap)
        if st[cur_idx]: continue
        st[cur_idx] = True
        i = h[cur_idx]
        while i != -1:
            wei = w[i]
            t = e[i]
            if dist[t] > dist[cur_idx] + wei:
                dist[t] = dist[cur_idx] + wei
                heappush(heap, [dist[t], t])
            i = ne[i]


for _ in range(m):
    a, b, wei = map(int, input().split())
    add(a, b, wei)

dijkstra()
for i in range(1, n + 1):
    print(-1, end=' ') if dist[i] == float('inf') else print(dist[i], end=' ')

# import heapq
# n, m = map(int,input().split())
# G=[[] for i in range(n+1)]
# w=[[] for i in range(n+1)]
# for i in range(m):
#     x,y,z = map(int,input().split())
#     G[x].append(y)
#     w[x].append(z)
# pre = [0]*(n+1)
# vis = [0]*(n+1)
# dis = [float('inf')]*(n+1)
# q = []
# dis[1]=0
# heapq.heappush(q, (0,1))
# while q:
#     u = heapq.heappop(q)[1]
#     if vis[u]:
#         continue
#     vis[u]=1
#     for i in range(len(G[u])):
#         v = G[u][i]
#         z = w[u][i]
#         if dis[v]>dis[u]+z:
#             dis[v]=dis[u]+z
#             heapq.heappush(q,(dis[v],v))
#             pre[v]=u
# for i in range(1,n+1):
#     if dis[i]>1<<64:
#         print(-1,end = ' ')
#     else:
#         print(dis[i],end = ' ')
