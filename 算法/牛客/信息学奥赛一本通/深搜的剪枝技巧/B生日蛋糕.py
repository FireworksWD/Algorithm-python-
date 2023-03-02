n = int(input())
m = int(input())
ans = 10 ** 9


def dfs(x, s, v, r, h):
    global ans
    if r < 0 or h < 0: return
    if ans < s: return
    if r * r * h * (m - x) + v < n: return
    if v > n: return
    if v == n and x == m:
        ans = min(ans, s)
        return
    for i in range(r - 1, m - x - 1, -1):
        for j in range(h - 1, m - x - 1, -1):
            dfs(x + 1, s + 2 * i * j, v + i * i * j, i, j)


for i in range(int(n ** 0.5), m - 1, -1):
    for j in range(n, m - 1, -1):
        dfs(1, i * i + i * j * 2, i * i * j, i, j)
print(ans)
