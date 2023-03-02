n = int(input())
a = [0] * 105
b = list(map(int, input().split()))
for i in range(len(b)):
    a[i + 1] = b[i]
tal = sum(a)
a.sort(reverse=True)
vis = [0] * 105
le = 0


def dfs(cnt, su, now):
    global le
    if su == le:
        su = 0
        now = 1
    if su == 0 and cnt == n:
        return True
    for i in range(now, n + 1):
        if vis[i]: continue
        if su+a[i]>le:continue
        vis[i] = 1
        if dfs(cnt + 1, su + a[i], i + 1): return True
        vis[i] = 0
        if su == 0: return False



for i in range(a[1], tal + 1):
    if tal % i == 0:
        le = i
        if dfs(0, 0, 1):
            print(i)
            exit()
