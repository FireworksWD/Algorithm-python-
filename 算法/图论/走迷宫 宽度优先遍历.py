'''给定一个n*m的二维整数数组，用来表示一个迷宫，数组中只包含0或1，其中0表示可以走的路，1表示不可通过的墙壁。
最初，有一个人位于左上角(1, 1)处，已知该人每次可以向上、下、左、右任意一个方向移动一个位置。
请问，该人从左上角移动至右下角(n, m)处，至少需要移动多少次。
数据保证(1, 1)处和(n, m)处的数字为0，且一定至少存在一条通路。
输入格式
第一行包含两个整数n和m。
接下来n行，每行包含m个整数（0或1），表示完整的二维数组迷宫。
输出格式
输出一个整数，表示从左上角移动至右下角的最少移动次数。
数据范围
1≤n,m≤1001≤n,m≤100
输入：
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
输出：
8
'''
n, m = 5, 5

lines = ['0 1 0 0 0',
         '0 1 0 1 0',
         '0 0 0 0 0',
         '0 1 1 1 0',
         '0 0 0 1 0']

grids = []
for i in range(n):
    grids.append(list(map(int, lines[i].split())))

move = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs():
    global n, m
    queue = [0] * (n * m)
    hh, tt = 0, 0
    queue[0] = [0, 0]
    res = 0
    grids[0][0] = -1
    while hh <= tt:
        res += 1
        for i in range(hh, tt + 1):
            x, y = queue[hh];
            hh += 1
            for oi, oj in move:
                xi, yj = x + oi, y + oj
                if not 0 <= xi < n or not 0 <= yj < m: continue
                if grids[xi][yj] == 1 or grids[xi][yj] == -1: continue
                if xi == n - 1 and yj == m - 1: return res
                tt += 1
                queue[tt] = [xi, yj]
                grids[xi][yj] = -1


print(bfs())