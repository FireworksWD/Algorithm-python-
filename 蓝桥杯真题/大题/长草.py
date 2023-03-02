import os
import sys

# 输入行n和列m
n, m = map(int, input().split())
# 创建一个一维数组，用于存储初始化后的草坪中的草的坐标
lawn = []
# 创建一个队列，用于存储未访问过的草的坐标
queue = []
# 循环输入每行
for i in range(n):
    lawn.append(list(map(str, input())))
    # 存储每行草的坐标
    for j in range(len(lawn[i])):
        if lawn[i][j] == 'g':
            queue.append([i, j])

# 输入多少个月
k = int(input())

if k == 0:
    for l in lawn:
        for row in l:
            print(row, end='\n')

# 循环每个月草生长情况
for month in range(k):
    lens = len(queue)
    for q in range(lens):
        # 取队列队首
        temp = queue.pop(0)

        # 草左边的格子
        x = temp[0]
        y = temp[1] - 1
        if 0 <= y < m and lawn[x][y] != 'g':
            queue.append([x, y])
            lawn[x][y] = 'g'

        # 草右边的格子
        y = temp[1] + 1
        if 0 <= y < m and lawn[x][y] != 'g':
            queue.append([x, y])
            lawn[x][y] = 'g'

        # 草下方的格子
        x = temp[0] + 1
        y = temp[1]
        if 0 <= x < n and lawn[x][y] != 'g':
            queue.append([x, y])
            lawn[x][y] = 'g'

        # 草上方的格子
        x = temp[0] - 1
        if 0 <= x < n and lawn[x][y] != 'g':
            queue.append([x, y])
            lawn[x][y] = 'g'

for i in range(n):
    for j in range(m):
        print(lawn[i][j], end='')
    print()
