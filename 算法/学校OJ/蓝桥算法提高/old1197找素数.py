x, y = map(int, input().split())


def solve(l, r):
    vis = [True] * (r + 1)
    res = []
    for i in range(l, r + 1):
        if vis[i]:
            res.append(i)
        for j in res:
            l = i * j
            if l >= r + 1:
                break
            vis[l] = False
            if i % j == 0:
                break
    return len(res)


print(solve(x, y))
