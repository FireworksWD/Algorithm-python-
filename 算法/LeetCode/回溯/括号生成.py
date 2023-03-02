'''数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
为了生成所有序列，我们可以使用递归。长度为 nnn 的序列就是在长度为 n−1n - 1n−1 的序列前加一个 ‘(’\text{`('}‘(’ 或 ‘)’\text{`)'}‘)’。

为了检查序列是否有效，我们遍历这个序列，并使用一个变量 balance\textit{balance}balance 表示左括号的数量减去右括号的数量。
如果在遍历过程中 balance\textit{balance}balance 的值小于零，或者结束时 balance\textit{balance}balance 的值不为零，
那么该序列就是无效的，否则它是有效的。
'''
# n = int(input())
# ans = []
#
#
# def geberate(A):
#     if len(A) == 2 * n:
#         if valid(A):
#             ans.append("".join(A))
#     else:
#         A.append("(")
#         geberate(A)
#         A.pop()
#         A.append(")")
#         geberate(A)
#         A.pop()
#
#
# def valid(A):
#     bal = 0
#     for c in A:
#         if c == "(":
#             bal += 1
#         else:
#             bal -= 1
#         if bal < 0:
#             return False
#     return bal == 0
#
#
# geberate([])
# print(ans)

#  回溯
#  如果左括号数量不大于 nnn，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以放一个右括号。
n = int(input())
ans = []


def backtrack(S: list, left, right):
    if len(S) == 2 * n:
        ans.append("".join(S))
        return
    if left < n:
        S.append('(')
        backtrack(S, left + 1, right)
        S.pop()
    if right < left:
        S.append(')')
        backtrack(S, left, right + 1)
        S.pop()


backtrack([], 0, 0)
print(ans)
