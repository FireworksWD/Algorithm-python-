n = int(input())

# 递归写法
# def dfs(k):
#     if k == 1:
#         return 'A'
#     return dfs(k - 1) + chr(65 + k - 1) + dfs(k - 1)
#
#
# print(dfs(n))

# 递推写法
s = ''
for i in range(0, n):
    t = s + chr(65 + i)
    s = t + s
print(s)
