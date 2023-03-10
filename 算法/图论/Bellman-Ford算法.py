'''给定一个n个点m条边的有向图，图中可能存在重边和自环， 边权可能为负数。
请你求出从1号点到n号点的最多经过k条边的最短距离，如果无法从1号点走到n号点，输出impossible。
注意：图中可能 存在负权回路 。
输入格式
第一行包含三个整数n，m，k。
接下来m行，每行包含三个整数x，y，z，表示存在一条从点x到点y的有向边，边长为z。
输出格式
输出一个整数，表示从1号点到n号点的最多经过k条边的最短距离。
如果不存在满足条件的路径，则输出“impossible”。
数据范围
1≤n,k≤500
1≤m≤10000
任意边长的绝对值不超过10000。
输入：
3 3 1
1 2 1
2 3 1
1 3 3
输出：
3
'''
n, m, k = map(int, input().split())
edges = []
dist = [float('inf')] * (n + 1)
for _ in range(m):
    edges.append(list(map(int, input().split())))


def bellmanFord(k):
    dist[1] = 0
    for _ in range(k):
        dist2 = dist.copy()
        for a, b, w in edges:
            dist[b] = min(dist[b], dist2[a] + w)


bellmanFord(k)
print('impossible') if dist[n] == float('inf') else print(dist[n])

