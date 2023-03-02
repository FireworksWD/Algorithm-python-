n = int(input())
ans = 0
a = [0, 1, 2, 3, 5, 7, 9]


def check(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def dfs(k, s):
    global ans
    if k > n:
        ans += 1
        # print(s)
        return
    for i in range(1, 7):
        if k == 1 and i == 1: continue
        if k != 1 and i == 2: continue
        x = s * 10 + a[i]
        if check(x):
            dfs(k + 1, x)


dfs(1, 0)
print(ans)
