import os
import sys

# 可以用图，进行计算
'''
1、构造一个关系矩阵
2、从第一个开始遍历，到最后可以放回原点，则存储到列表
3、
注：
  如果遍历过程中回到之前的点，则截至
'''
# """
# 按照题目描述，很容易理解成x崇拜的人位于x的右边，也就是这组整数相邻的人构成崇拜关系，
# 然而结合图形和输入的N个整数，发现如果将这些整数看成是一个数组nums，那么构成崇拜关系的规律应该是x崇拜nums[x-1]
# """
# n = int(input())
# nums = [0] + list(map(int,input().split()))

# max_ = 0
# for i in range(1,len(nums)):
#   con = 0
#   lst = []
#   x = nums[i]
#   while x not in lst:
#     lst.append(x)
#     x = nums[x]
#     con += 1
#     if con > max_:
#       max_ = con
#
# print(max_)
sys.setrecursionlimit(1000000)
n = int(input())
f = [0] + list(map(int, input().split()))
vis = [0] * (n + 1)  # 存储崇拜者顺序，1表示第一个小朋友，2表示前一个小朋友崇拜的对象所在的位置下标
ans = 0


def dfs(u, i):
    if vis[u]:  # vis[u]访问过
        global ans
        ans = max(ans, i - vis[u])  # 用当前列表长度i减去已经在T中的那个小朋友的下标
        return
    vis[u] = i  #
    dfs(f[u], i + 1)  # f[u]:寻找下一个崇拜者  i+1:当前构成环的长度+1


for i in range(1, n + 1):
    if not vis[i]:
        dfs(i, 1)  # 从i开始遍历，环默认为1
        # print(vis)
# vis的全部情况
# [0, 1, 3, 2, 4, 5, 0, 0, 0, 0]
# [0, 1, 3, 2, 4, 5, 1, 0, 2, 0]
# [0, 1, 3, 2, 4, 5, 1, 1, 2, 0]
# [0, 1, 3, 2, 4, 5, 1, 1, 2, 1]
print(ans)
