n, k = map(int, input().split())
ans = 0


def dfs(target, t, path: list):
    global ans
    if target == 0 and len(path) == k:
        # print(path[:])
        ans += 1
        return
    if target < 0:
        return
    for i in range(t, n + 1):
        dfs(target - i, i, path + [i])


dfs(n, 1, [])
print(ans)

# n1, k1 = map(int, input().split())
#
#
# def dfs(n, k):
#     if n == k or k == 1:
#         return 1
#     if n < k:
#         return 0
#     return dfs(n - 1, k - 1) + dfs(n - k, k)
#
#
# print(dfs(n1, k1))vfgb b
