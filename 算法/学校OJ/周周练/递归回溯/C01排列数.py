'''0、1、2三个数字的全排列有六种，按照字母序排列如下：
012、021、102、120、201、210
输入一个数n，求0~9十个数的全排列中的第n个（第1个为0123456789）。


输入
一行，包含一个整数n


输出
一行，包含一组10个数字的全排列'''
# n = int(input())
# vis = [False] * 10
# res = []
# ans = 0
# flage = False
#
#
# def backtrack(index):
#     global ans
#     global flage
#     if index == 10:
#         ans += 1
#         if ans == n:
#             for i in res:
#                 print(i, end='')
#                 flage = True
#     if flage:
#         return
#     for i in range(10):
#         if not vis[i]:
#             vis[i] = True
#             res.append(i)
#             backtrack(index + 1)
#             vis[i] = False
#             res.pop()
#
#
# backtrack(0)
import itertools

n = int(input())
s = [i for i in range(10)]
t = 0
for x in itertools.permutations(s):
    t += 1
    if t == n:
        for i in x:
            print(i, end='')
        break
