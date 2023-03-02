'''现在，有一个n级台阶的楼梯，每级台阶上都有若干个石子，其中第ii级台阶上有ai个石子(i≥1)。
两位玩家轮流操作，每次操作可以从任意一级台阶上拿若干个石子放到下一级台阶中（不能不拿）。
已经拿到地面上的石子不能再拿，最后无法进行操作的人视为失败。
问如果两人都采用最优策略，先手是否必胜
'''

# 结论：与奇数石堆有关，与偶数石堆无关。
n = int(input())
nums = list(map(int, input().split()))

res = 0
for i in range(n):
    if i % 2 == 0:
        res ^= nums[i]

if res == 0:
    print('No')
else:
    print('Yes')