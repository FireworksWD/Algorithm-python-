a_ = list(map(int, input().split()))
n, m = a_[0], a_[1]
a = a_[2:]
a.sort()
res = 0


def dfs(k, su):
    global res
    if k >= n:
        return
    x = su + a[k]
    if x == m:
        res += 1
        return
    if x > m:
        return
    dfs(k + 1, x)
    dfs(k + 1, su)


dfs(0, 0)
print(res)

# al = list(map(int, input().split()))
# n, m = al[0], al[1]
# a = al[2:]
# ans = 0
#
#
# def dfs(k, target):
#     global ans
#     if target<0:
#         return
#     if target == 0:
#         ans += 1
#         return
#     if k == n: return
#     for i in range(k, n):
#         dfs(i + 1, target - a[i])
#
#
# dfs(0, m)
# print(ans)
