'''给定一个n个点m条边的无向图，图中可能存在重边和自环，边权可能为负数。
求最小生成树的树边权重之和，如果最小生成树不存在则输出impossible。
给定一张边带权的无向图G=(V, E)，其中V表示图中点的集合，E表示图中边的集合，n=|V|，m=|E|。
由V中的全部n个顶点和E中n-1条边构成的无向连通子图被称为G的一棵生成树，其中边的权值之和最小的生成树被称为无向图G的最小生成树。
输入格式
第一行包含两个整数n和m。
接下来m行，每行包含三个整数u，v，w，表示点u和点v之间存在一条权值为w的边。
输出格式
共一行，若存在最小生成树，则输出一个整数，表示最小生成树的树边权重之和，如果最小生成树不存在则输出impossible。
数据范围
1≤n≤500
1≤m≤10^5
图中涉及边的边权的绝对值均不超过10000。
输入：
4 5
1 2 1
1 3 2
1 4 3
2 3 2
3 4 4
输出：
6
'''
n, m = map(int, input().split())
edges = []
pre = list(range(n + 1))


def find(x):
    root = x
    while root != pre[root]: root = pre[root]
    while x != root: pre[x], x = root, pre[x]
    return root


for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])

edges.sort(lambda x: x[2])


def kruskal():
    global n
    cnt = 0
    res = 0
    for u, v, w in edges:
        rootu, rootv = find(u), find(v)
        if rootu != rootv:  # 合并
            pre[rootv] = rootu
            cnt += 1
            res += w
        if cnt == n - 1: return res  # 最小生成树的边为n-1
    return 'impossible'


print(kruskal())