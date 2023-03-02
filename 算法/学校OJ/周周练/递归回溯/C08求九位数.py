vis = [False] * 10  # 设置标记数组
res = []  # 临时数组
flage = False  # 定义一个哨兵


def check(temp: list):  # 判断是否满足题意
    t = 0
    for i in range(1, 10):  # 这里利用下标表示1-9，
        t = temp[i - 1] + t * 10  # 这里表示前i位
        if t % i != 0:  # 判断是否被整除
            return False
    return True


def dfs(t):
    global flage  # 全局变量
    if t == 9:  # 出口
        if check(res):  # 判断
            for i in res:  # 打印结果
                print(i, end='')
            flage = True  # 置位True
        return
    if flage: return  # 满足条件直接终止
    for i in range(1, 10):  # 1-9的全排列
        if not vis[i]:  # 如果没搜索过
            vis[i] = True
            res.append(i)
            dfs(t + 1)  # 下一步搜索
            res.pop()
            vis[i] = False  # 回溯


dfs(0)  # 开始搜索
