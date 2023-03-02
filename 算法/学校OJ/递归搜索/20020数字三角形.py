n, ans = int(input()), 0
vis = [False] * 10
res = []


def check(a):
    if a[0] < a[5] < a[8] and a[1] < a[3] and a[6] < a[7] and a[2] < a[4] and a[0] + a[1] + a[3] + a[5] == a[5] + a[6] + \
            a[7] + a[8] and a[0] + a[2] + a[4] + a[8] == a[0] + a[1] + a[3] + a[5] and a[0] + a[1] + a[3] + a[5] == n:
        return True
    return False


def dfs(t):
    global ans
    if t == 10:
        if check(res):
            ans += 1
        return
    for i in range(1, 10):
        if vis[i]: continue
        vis[i] = True
        res.append(i)
        dfs(t + 1)
        vis[i] = False
        res.pop()


dfs(1)
print(ans)
