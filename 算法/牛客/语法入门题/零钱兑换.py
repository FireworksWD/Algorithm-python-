a = [1, 2, 5]
n = int(input())
ans = 0


def dfs(k, target):
    global ans
    if target < 0:
        return
    if target == 0:
        ans += 1
        return
    if k >= 3:
        return
    for i in range(k, 3):
        dfs(i, target - a[i])


dfs(0, n)
print(ans)