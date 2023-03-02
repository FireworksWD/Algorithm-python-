n1, k1 = map(int, input().split())


def dfs(n, k):
    if n == k or k == 1:
        return 1
    if n < k:
        return 0
    return dfs(n - 1, k - 1) + dfs(n - k, k)


print(dfs(n1, k1))
