'''给定一个n个点m条边的无向图，图中可能存在重边和自环。
请你判断这个图是否是二分图。
输入格式
第一行包含两个整数n和m。
接下来m行，每行包含两个整数u和v，表示点u和点v之间存在一条边。
输出格式
如果给定图是二分图，则输出“Yes”，否则输出“No”。
数据范围
1≤n,m≤10^5
输入：
4 4
1 3
1 4
2 3
2 4
输出：
Yes
'''
n, m = map(int, input().split())
st = [0] * (n + 1)  # 染色数组
idx = 0
e, ne = [0] * (2 * m + 1), [0] * (2 * m + 1)
h = [-1] * (n + 1)


def add(a, b):
    global idx
    e[idx], h[a], ne[idx] = b, idx, h[a]
    idx += 1


def bfs(i, c):
    queue = [(i, c)]
    hh, tt = 0, 0
    st[i] = c
    while hh <= tt:
        t, c = queue[hh]
        hh += 1
        i = h[t]
        while i != -1:
            j = e[i]
            if st[j] == 0:
                st[j] = 3 - c
                queue.append((j, 3 - c))
                tt += 1
            elif st[j] == c:
                return False
            i = ne[i]
    return True


for _ in range(m):
    a, b = map(int, input().split())
    add(a, b)
    add(b, a)

flag = True
for i in range(1, n + 1):
    if st[i] == 0 and not bfs(i, 1):
        flag = False;
        break
if flag:
    print('Yes')
else:
    print('No')