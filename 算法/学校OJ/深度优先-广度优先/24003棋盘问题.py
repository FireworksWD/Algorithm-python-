n, k = map(int, input().split())
vis = [0] * 20
ans = 0
char = []
for i in range(n):
    char.append(list(input()))


def dfs(row, t):
    global ans
    if t > k:
        ans += 1
        return
    for i in range(row, n):
        for j in range(0, n):
            if char[i][j] == '.' or vis[j] == 1:
                continue
            vis[j] = 1
            dfs(i + 1, t + 1)
            vis[j] = 0


dfs(0, 1)
print(ans)
