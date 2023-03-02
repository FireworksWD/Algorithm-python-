al = list(map(int, input().split()))
n, m = al[0], al[1]
value = []
for i in range(2, len(al), m):
    value.append(al[i:i+m])
# res=[0]*n # 具体方案下标表示人，值表示第几项工作
max_value = 0
vis = [False] * n


def dfs(k, path):
    global max_value
    if k == n:
        max_value = max(max_value, path)
        return
    for i in range(m):
        if vis[i]: continue
        # res[k]=i # k个人做第i项工作
        vis[i] = True
        dfs(k + 1, path + value[k][i])
        vis[i] = False


dfs(0, 0)
print(max_value)
