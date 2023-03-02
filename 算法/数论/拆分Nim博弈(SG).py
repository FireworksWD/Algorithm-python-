'''给定n堆石子，两位玩家轮流操作，每次操作可以取走其中的一堆石子，然后放入两堆规模更小的石子（新堆规模可以为0，且两个新堆的石子总数可以大于取走的那堆石子数），最后无法进行操作的人视为失败。
问如果两人都采用最优策略，先手是否必胜。
输入格式
第一行包含整数n。
第二行包含n个整数，其中第ii个整数表示第ii堆石子的数量ai。
输出格式
如果先手方必胜，则输出“Yes”。
否则，输出“No”。
'''

n = int(input())
stones = list(map(int, input().split()))

labels = [-1] * 200


def sg(stone):
    if labels[stone] != -1: return labels[stone]
    connect = set()
    for i in range(stone):
        for j in range(i + 1):
            connect.add(sg(i) ^ sg(j))
    i = 0
    while True:
        if i not in connect:
            labels[stone] = i
            break
        i += 1
    return labels[stone]


res = 0
for stone in stones:
    res ^= sg(stone)

if res == 0:
    print('No')
else:
    print('Yes')