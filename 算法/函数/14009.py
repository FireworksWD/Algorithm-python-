res = 0


def dfs(k, source):
    global res
    if k > 10:
        if source == 90:
            res += 1
        return
    for i in range(11):
        if i + source > 90: continue
        if i + source == 90:
            res += 1
            continue
        if k * 10 - i - source > 10:
            continue
        dfs(k + 1, i + source)


dfs(1, 0)
print(res)