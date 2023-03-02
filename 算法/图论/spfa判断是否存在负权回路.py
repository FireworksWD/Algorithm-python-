'''给定一个n个点m条边的有向图，图中可能存在重边和自环， 边权可能为负数。
请你判断图中是否存在负权回路。
输入格式
第一行包含整数n和m。
接下来m行每行包含三个整数x，y，z，表示存在一条从点x到点y的有向边，边长为z。
输出格式
如果图中存在负权回路，则输出“Yes”，否则输出“No”。
数据范围
1≤n≤2000
1≤m≤10000
图中涉及边长绝对值均不超过10000。
输入：
3 3
1 2 -1
2 3 4
3 1 -4
输出：
Yes
'''
n, m = map(int, input().split())
h = [-1] * (2 * m + 1)

e, ne, w = [0] * (2 * m + 1), [0] * (2 * m + 1), [0] * (2 * m + 1)
idx = 0
cnt = [0] * (n + 1)  # 用来记录当前路径走了多少步

st = [True] * (n + 1)  # 一开始都在里面
dist = [0] * (n + 1)  # 所有点起始距离都为0，这样可以更好找负权回路


def add(a, b, wei):
    global idx
    e[idx], ne[idx], w[idx], h[a] = b, h[a], wei, idx
    idx += 1


for _ in range(m):
    a, b, wei = map(int, input().split())
    add(a, b, wei)


def spfa():
    global n
    queue = list(range(1, n + 1))  # 每个点都要作为中间点，防止不连通
    hh, tt = 0, n - 1
    while hh <= tt:
        t = queue[hh];
        hh += 1
        st[t] = False
        i = h[t]
        while i != -1:
            j, wei = e[i], w[i]
            if dist[j] > dist[t] + wei:
                dist[j] = dist[t] + wei
                cnt[j] = cnt[t] + 1
                if cnt[j] >= n: return True
                if not st[j]:
                    queue.append(j);
                    tt += 1
                    st[j] = True
            i = ne[i]
    return False


if spfa():
    print('Yes')
else:
    print('No')