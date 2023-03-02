'''给定一个n个点m条边的有向图，图中可能存在重边和自环，边权可能为负数。
再给定k个询问，每个询问包含两个整数x和y，表示查询从点x到点y的最短距离，如果路径不存在，则输出“impossible”。
数据保证图中不存在负权回路。
输入格式
第一行包含三个整数n，m，k
接下来m行，每行包含三个整数x，y，z，表示存在一条从点x到点y的有向边，边长为z。
接下来k行，每行包含两个整数x，y，表示询问点x到点y的最短距离。
输出格式
共k行，每行输出一个整数，表示询问的结果，若询问两点间不存在路径，则输出“impossible”。
数据范围
1≤n≤200
1≤k≤n^2
1≤m≤20000
图中涉及边长绝对值均不超过10000。
输入：
3 3 2
1 2 1
2 3 2
1 3 1
2 1
1 3
输出：
impossible
1
'''
n, m, k = map(int, input().split())
dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    dist[x][y] = min(dist[x][y], z)

for i in range(1, n + 1):
    dist[i][i] = 0


def floyd():
    global n
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])


floyd()

for _ in range(k):
    x, y = map(int, input().split())
    if dist[x][y] == float('inf'):
        print('impossible')
    else:
        print(dist[x][y])