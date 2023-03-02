n, w = map(int, input().split())
w_lis = []
cab = [0] * 20
for i in range(n):
    w_lis.append(int(input()))
w_lis.sort(reverse=True)
ans = n


def dfs(k, tw):
    global ans
    if tw >= ans: return
    if k == n:
        ans = min(ans, tw)
        return
    for i in range(tw):
        if cab[i] + w_lis[k] <= w:
            cab[i] += w_lis[k]
            dfs(k + 1, tw)
            cab[i] -= w_lis[k]
    cab[tw + 1] = w_lis[k]
    dfs(k + 1, tw + 1)
    cab[tw + 1] = 0


dfs(0, 0)
print(ans)
