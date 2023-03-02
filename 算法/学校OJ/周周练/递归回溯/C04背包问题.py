'''问题：假设有n件质量分配为w1，w2，...，wn的物品和一个最多能装载总质量为T的背包，
能否从这n件物品中选择若干件物品装入背包，使得被选物品的总质量恰好等于背包所能装载的最大质量，
即wi1+wi2+...+wik=T。若能，则背包问题有解，否则无解。
(例如：有5件可选物品，质量分别为8千克、4千克、3千克、5千克、1千克。
假设背包的最大转载质量是10千克。)
输入
一行物品总个数n和背包能装的总质量T；用空格隔开
第二行:是n个正整数，代表n个物品的质量w【i】，用空格隔开
输出
一个正整数，若有解输出1，否则输出0'''
# a1 = list(map(int, input().split()))
# n, t = a1[0], a1[1]
# bag = a1[2:]
#
#
# def dfs(k, t):
#     if t == 0:
#         return True
#     if k == n:
#         return False
#     if t < 0:
#         return False
#     if dfs(k + 1, t - bag[k]):
#         return True
#     return dfs(k + 1, t)
#
#
# if dfs(0, t):
#     print(1)
# else:
#     print(0)

a1 = list(map(int, input().split()))
n, t = a1[0], a1[1]
bag = a1[1:]
dp = [0] * 1001
dp[0] = 1
for i in range(1, n + 1):
    for j in range(t, bag[i] - 1, -1):
        dp[j] += dp[j - bag[i]]
if dp[t] > 0:
    print(1)
else:
    print(0)
