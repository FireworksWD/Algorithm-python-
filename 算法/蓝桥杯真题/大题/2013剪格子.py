m, n = map(int, input().split())
a = []
k = 0
for i in range(n):
    a1 = list(map(int, input().split()))
    k += sum(a1)
    a.append(a1)
div = [[1, 0], [0, 1], [-1, 0], [0, -1]]
b = [[False for _ in range(m)] for _ in range(n)]
max1 = 100


def dfs(x, y, num, sum1):
    global max1, a, b
    if sum1 == k / 2 and num < max1:
        max1 = num
        return max1
    for i in range(4):
        dx = x + div[i][0]
        dy = y + div[i][1]
        if 0 <= dx < n and 0 <= dy < m and b[dx][dy] == False:
            b[dx][dy] = True
            dfs(dx, dy, num + 1, sum1 + a[dx][dy])
            b[dx][dy] = False


b[0][0] = True
dfs(0, 0, 1, a[0][0])
print(max1)
