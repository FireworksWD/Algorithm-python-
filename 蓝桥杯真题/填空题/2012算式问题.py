# vis = [0] * 10
# ans = 0
#
#
# def dfs(k, path: list):
#     global ans
#     if k > 9:
#         if int(''.join(path[:3])) + int(''.join(path[3:6])) == int(''.join(path[6:9])):
#             ans += 1
#         return
#     for i in range(1, 10):
#         if vis[i]: continue
#         vis[i] += 1
#         path.append(str(i))
#         dfs(k + 1, path)
#         vis[i] -= 1
#         path.pop()
#
#
# dfs(1, [])
# print(ans)

import itertools

ans = 0
for i in itertools.permutations('123456789'):
    x = ''.join(list(i))
    a, b, c = int(x[:3]), int(x[3:6]), int(x[6:9])
    if a + b == c:
        ans += 1
print(ans)
