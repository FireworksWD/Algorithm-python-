vis = [False] * 10
res = []


def dfs(k):
    if k == 10:
        if ((res[0] * 1000 + res[1] * 100 + res[2] * 10 + res[3]) - (
                res[4] * 1000 + res[5] * 100 + res[6] * 10 + res[7])) * (res[8] * 10 + res[9]) == 900 and res[
            0] != 0 and res[4] != 0 and res[8] != 0:
            print(f'{res[0] * 1000 + res[1] * 100 + res[2] * 10 + res[3]} '
                  f'{res[4] * 1000 + res[5] * 100 + res[6] * 10 + res[7]} '
                  f'{res[8] * 10 + res[9]}')
        return
    for i in range(10):
        if vis[i]: continue
        vis[i] = True
        res.append(i)
        dfs(k + 1)
        res.pop()
        vis[i] = False


dfs(0)
