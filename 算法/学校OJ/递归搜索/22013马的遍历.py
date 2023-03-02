n, m = map(int, input().split())
ans = 0
dir = [[2, 1], [1, 2], [-1, 2], [-2, 1]]


def dfs(x, y):
    global ans
    if x > n or y > m:
        return
    if x == n and y == m:
        ans += 1
        return
    for xx, yy in dir:
        tx = x + xx
        ty = y + yy
        if tx >= 0 and tx <= n and ty >= 0 and ty <= m:
            dfs(tx, ty)


dfs(0, 0)
print(ans)
