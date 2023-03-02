n = int(input())
s = ['A', 'B', 'C']
ans = 0


def check(lis: list):
    for i in range(len(lis) - 3):
        if lis[i] + lis[i + 1] == lis[i + 2] + lis[i + 3]:
            return False
    return True


def dfs(path: list, t):
    global ans
    if t == n:
        if check(path[:]):
            # print(' '.join(path[:]))
            ans += 1
        return
    for i in range(3):
        dfs(path + [s[i]], t + 1)


dfs([], 0)
print(ans)
