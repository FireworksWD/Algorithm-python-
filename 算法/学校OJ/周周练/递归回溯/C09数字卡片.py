n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
vis = [False] * 10


def pd(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def dfs(k, s):
    global ans
    if k >= m:
        if pd(s): ans += 1
        return
    if pd(s): ans += 1
    for i in range(n):
        x = s * 10 + a[i]
        if vis[i]: continue
        vis[i] = True
        dfs(k + 1, x)
        vis[i] = False


dfs(0, 0)
print(ans)
