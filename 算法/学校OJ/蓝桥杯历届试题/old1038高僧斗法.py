loc = [int(i) for i in input().split()]  # 记录小和尚位置
n = len(loc)
group = [loc[i] - loc[i - 1] - 1 for i in range(1, n)]  # 相邻的小和尚两两配对，计算距离
# 求异或结果
s = 0
for i in range(0, len(group), 2):
    s ^= group[i]

if s == 0:  # 若开局异或结果为0，则必输无疑
    print(-1)
else:
    for i in range(n - 1):  # 遍历每个小和尚，寻找可以使结果为0的移动方案
        for j in range(1, loc[i + 1] - loc[i]):  # 前进步数
            group[i] -= j
            if i != 0:
                group[i - 1] += j
            s = 0
            for k in range(0, len(group), 2):
                s ^= group[k]
            if s == 0:  # 找到可以赢的方案
                print(loc[i], loc[i] + j)
                exit()
            group[i] += j  # 若当前方案非可以胜利的方案，则需要恢复
            if i != 0:
                group[i - 1] -= j
