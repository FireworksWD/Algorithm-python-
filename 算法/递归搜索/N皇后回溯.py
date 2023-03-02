n = int(input('输入棋盘大小(≤8):'))
# rec = [] # 定义二维数组存放皇后放置的位置信息
count = 0  # 用于记录可能的情况
def Check_bool(y, x, rec):  # 主要是检查不能在同一行不能在同一列不能在正负对角线
    for j in rec:  # 放过的每个皇后的坐标与当前皇后依次判断
        if abs(j[1] - x) == abs(j[0] - y) or y == j[0] or x == j[1]:  # j[0]代表已经放置皇后的横坐标，j[1]纵坐标
            return False
    return True
def dfs(y, x, rec):  # y代表行(横坐标)，x代表列(纵坐标)，第三个代表存放皇后的解集(皇后的坐标)
    global count
    if y == n - 1:
        print(rec)  # 出口
        count += 1
        return
    if y > n - 1 or x > n - 1:  # 越界
        return
    for i in range(n):
        if Check_bool(y + 1, i, rec):  # 试探
            rec.append([y + 1, i])  # 添加皇后坐标
            dfs(y + 1, i, rec)  # 下一行
            rec.pop(-1)  # 回溯
for k in range(n):
    dfs(0, k, rec=[[0, k]])
print(count)
