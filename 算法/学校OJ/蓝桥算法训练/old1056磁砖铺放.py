target = int(input())
ans = 0
a = [1, 2]
def dfs(k, target, path: list):
    global ans
    if target == 0:
        # print(path[:])
        ans += 1
        return
    if target < 0:
        return
    for i in range(0, 2):
        dfs(i, target - a[i], path + [a[i]])
dfs(0, target, [])
print(ans)
