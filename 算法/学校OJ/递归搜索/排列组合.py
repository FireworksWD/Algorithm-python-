# 全排列 例如我们生成1-4的全排列
vis = [False] * 5  # 标记数组，看是否被搜索过
res = []  # 结果，将找到的每一种存放到res中


def backtrack(t, path, n):  # k表示深度，path表示临时存放一种组合的数组,n表示选择的个数
    if len(path) == n:  #
        res.append(path[:])  # 选择的n个数
        return  # 结束
    for i in range(t, 5):  # 保证前面的数小于后面的数
        if not vis[i]:  # 如果没有使用过当前数字
            vis[i] = True  # 选择
            path.append(i)  # 将该数添加到path中
            backtrack(i + 1, path, n)  # 下一步搜索
            path.pop()
            vis[i] = False  # 回溯


backtrack(1, [], 3)  # 例如从1-4中选三个数
for i in res:
    print(i)
