'''
给定一颗树，树中包含n个结点（编号1~n）和n-1条无向边。
请你找到树的重心，并输出将重心删除后，剩余各个连通块中点数的最大值。
重心定义：重心是指树中的一个结点，如果将这个点删除后，剩余各个连通块中点数的最大值最小，那么这个节点被称为树的重心。
输入格式
第一行包含整数n，表示树的结点数。
接下来n-1行，每行包含两个整数a和b，表示点a和点b之间存在一条边。
输出格式
输出一个整数m，表示将重心删除后，剩余各个连通块中点数的最大值。
数据范围
1≤n≤10
输入：
9
1 2
1 7
1 4
2 8
2 5
4 3
3 9
4 6
输出：
4
'''
n = int(input())
idx = 0
h, e, ne = [-1] * (n + 1), [0] * (2 * n + 2), [0] * (2 * n + 2)
st = [False] * (n + 1)
min_num = n


def add(a, b):
    global idx
    e[idx] = b
    h[a], ne[idx] = idx, h[a]
    idx += 1


def dfs(cur_idx):
    global min_num, n
    st[cur_idx], sum1, i, res = True, 1, h[cur_idx], 0
    while i != -1:
        next_idx = e[i]
        if not st[next_idx]:
            s = dfs(next_idx)
            res = max(res, s)
            sum1 += s
        i = ne[i]
    res = max(res, n - sum1)
    min_num = min(res, min_num)
    return sum1


for i in range(n - 1):
    a, b = map(int, input().split())
    add(a, b)
    add(b, a)

dfs(1)
print(min_num)

