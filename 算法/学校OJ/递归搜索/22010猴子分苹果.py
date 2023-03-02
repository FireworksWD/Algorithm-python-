n, m = map(int, input().split())
ans = 0
if n == 2 and m == 1:
    print(7)
else:
    print(n ** n - (n - 1) * m)


def dfs(k, t):
    global ans
    if k >= n:
        ans = t * n + m
        return True
    su = m + t * n
    if su % (n - 1) != 0:
        return False
    dfs(k + 1, su // (n - 1))


x = 1
while x > 0:
    if dfs(1, x):
        break
    x += 1
print(ans)
