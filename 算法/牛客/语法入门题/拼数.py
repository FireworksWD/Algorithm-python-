n = int(input())
l = list(map(int, input().split(" ")))


def max_sort(l):
    # 将列表的长度赋值给变量n
    m = len(l)
    for i in range(m - 1):
        # 内层循环控制比较的次数，每轮会确定排在列表末尾的一个值
        for j in range(m - 1 - i):
            # 每次将列表相邻两个元素转换成字符串使用+号连接起来，然后互换位置连接起来，再比较大小
            if str(l[j]) + str(l[j + 1]) < str(l[j + 1]) + str(l[j]):
                # 如果互换位置组合的数字大于初始位置组合的数字，则两个元素互换位置
                l[j], l[j + 1] = l[j + 1], l[j]
    # 定义一个空字符串
    t = ''
    # 遍历排好序的列表
    for p in l:
        # 将列表内的所有元素依次连接组合起来，返回时转换为数字类型
        t += str(p)
    return int(t)


print(max_sort(l))
