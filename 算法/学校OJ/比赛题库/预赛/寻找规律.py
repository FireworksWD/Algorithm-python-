x, y, z = map(int, input().split())
vis = [False] * 10
ans = 0


def chevk(a: list):
    t1 = a[0] * 100 + a[1] * 10 + a[2]
    t2 = a[3] * 100 + a[4] * 10 + a[5]
    t3 = a[6] * 100 + a[7] * 10 + a[8]
    if t2 / t1 == y / x and t3 / t1 == z / x and t3 / t2 == z / y:
        return True
    return False


def dfs(k, path: list):
    global ans
    if k == 10:
        if chevk(path[:]):
            ans += 1
        return
    for i in range(1, 10):
        if vis[i]: continue
        vis[i] = True
        path.append(i)
        dfs(k + 1, path)
        vis[i] = False
        path.pop()


dfs(1, [])
print(ans)
