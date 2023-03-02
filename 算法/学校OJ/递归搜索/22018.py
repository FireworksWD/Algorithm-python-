all_n = list(map(int, input().split()))
n, c = all_n[0], all_n[1]
a = all_n[2:]
a.sort()
Max = 0
flage = False


def dfs(k, su):
    global Max
    global flage
    if k >= n:
        if su < c:
            Max = max(su, Max)
        return
    if flage:
        return
    x = su + a[k]
    if x == c:
        Max = c
        flage = True
        return
    if x > c:
        Max = max(Max, su)
        return
    dfs(k + 1, x)
    dfs(k + 1, su)


dfs(0, 0)
print(Max)
