'''给定一个n个点m条边的有向图，图中可能存在重边和自环。
所有边的长度都是1，点的编号为1~n。
请你求出1号点到n号点的最短距离，如果从1号点无法走到n号点，输出-1。
输入格式
第一行包含两个整数n和m。
接下来m行，每行包含两个整数a和b，表示存在一条从a走到b的长度为1的边。
输出格式
输出一个整数，表示1号点到n号点的最短距离。
数据范围
1≤n,m≤10^5
输入：
4 5
1 2
2 3
3 4
1 3
1 4
输出：
1
'''
n, m = map(int, input().split())

idx = 0
h, e, ne = [-1] * (n + 1), [0] * (2 * m + 1), [0] * (2 * m + 1)
st = [False] * (n + 1)  # 防止自环和重边


def add(a, b):
    global idx
    e[idx] = b
    h[a], ne[idx] = idx, h[a]
    idx += 1


def bfs():
    global n
    queue = [1]
    hh, tt = 0, 0
    res = 0
    while hh <= tt:
        res += 1
        for _ in range(hh, tt + 1):
            cur = queue[hh];
            hh += 1
            i = h[cur]
            while i != -1:
                j = e[i]
                if j == n: return res
                if not st[j]:
                    queue.append(j);
                    tt += 1
                    st[j] = True
                i = ne[i]
    return -1


for _ in range(m):
    a, b = map(int, input().split())
    add(a, b)

print(bfs())