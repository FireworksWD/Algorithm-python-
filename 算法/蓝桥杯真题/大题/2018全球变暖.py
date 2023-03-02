import os
import sys

# 请在此输入您的代码
# 用 DFS 或 BFS 搜出有多少个岛（连通块），检查这个岛有没有高地，统计那些没有高地
# 的岛（连通块）的数量，就是答案。
n = int(input())
a = []
for i in range(n):
    a.append(input())

vis = [[0] * n for i in range(n)]  # 记录是否访问过的数组
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 记录左右下上四个方向
flag = True
q = []  # 用列表来实现队列


def bfs(x, y):
    global flag
    q.append((x, y))
    vis[x][y] = 1
    while len(q):
        item = q.pop(0)  # 将队列中第一个元素出队
        tx = item[0]
        ty = item[1]
        if a[tx][ty + 1] == '#' and a[tx][ty - 1] == '#' and a[tx + 1][ty] == '#' and a[tx - 1][ty] == '#':
            flag = False  # 这是一个高地，不会被淹没
        for i in range(4):
            nx = tx + dir[i][0]
            ny = ty + dir[i][1]
            if vis[nx][ny] == 0 and a[nx][ny] == '#':
                vis[nx][ny] = 1
                q.append((nx, ny))


ans = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == '#' and vis[i][j] == 0:
            flag = True  # 假设这个岛被淹
            bfs(i, j)  # 找这个岛中有没有高地，如果有flag为True
            if flag:
                ans += 1  # 会被淹没的岛数量加1

print(ans)
