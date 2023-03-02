'''给定一个n个点m条边的有向图，图中可能存在重边和自环， 边权可能为负数。
请你求出1号点到n号点的最短距离，如果无法从1号点走到n号点，则输出impossible。
数据保证不存在负权回路。
输入格式
第一行包含整数n和m。
接下来m行每行包含三个整数x，y，z，表示存在一条从点x到点y的有向边，边长为z
输出格式
输出一个整数，表示1号点到n号点的最短距离。
如果路径不存在，则输出”impossible”。
数据范围
1≤n,m≤10^5
图中涉及边长绝对值均不超过10000。
输入：
3 3
1 2 5
2 3 -3
1 3 4
输出：
2
'''
n, m = map(int, input().split())
idx = 0
h = [-1] * (n + 1)
e, ne, w = [0] * (2 * m + 1), [0] * (2 * m + 1), [0] * (2 * m + 1)
dist = [float('inf')] * (n + 1)


def add(a, b, wei):
    global idx
    e[idx], w[idx] = b, wei
    h[a], ne[idx] = idx, h[a]
    idx += 1


def spfa():
    queue = [1]
    st = [False] * (n + 1)  # 用来判断当前点是否在队列中
    dist[1] = 0
    hh, tt = 0, 0
    while hh <= tt:
        t = queue[hh];
        hh += 1
        st[t] = False
        i = h[t]
        while i != -1:
            j, wei = e[i], w[i]
            if dist[j] > dist[t] + wei:
                dist[j] = dist[t] + wei
                if not st[j]:
                    queue.append(j)
                    st[j] = True
                    tt += 1
            i = ne[i]


for _ in range(m):
    a, b, wei = map(int, input().split())
    add(a, b, wei)

spfa()
if dist[n] == float('inf'):
    print('impossible')
else:
    print(dist[n])