'''给定n堆石子以及一个由k个不同正整数构成的数字集合S。
现在有两位玩家轮流操作，每次操作可以从任意一堆石子中拿取石子，每次拿取的石子数量必须包含于集合S，最后无法进行操作的人视为失败。
问如果两人都采用最优策略，先手是否必胜。
输入格式
第一行包含整数k，表示数字集合S中数字的个数。
第二行包含k个整数，其中第ii个整数表示数字集合S中的第i个数si。
第三行包含整数n。
第四行包含n个整数，其中第ii个整数表示第ii堆石子的数量hi。
输出格式
如果先手方必胜，则输出“Yes”。
否则，输出“No”'''

k = int(input())
takes = list(map(int, input().split()))
n = int(input())
stones = list(map(int, input().split()))

labels = [-1] * (10010)  # 用于标记当前节点的sg值


def sg(x):
    if labels[x] != -1: return labels[x]
    connect = set()  # 用于记录连接的sg值
    for t in takes:
        if x - t >= 0: connect.add(sg(x - t))
    i = 0
    while True:
        if i not in connect:
            labels[x] = i
            break
        i += 1
    return labels[x]


res = 0
for s in stones:
    res ^= sg(s)

if res == 0:
    print('No')
else:
    print('Yes')