t = int(input())
a = []
for i in range(2 * t):
    a.append(int(input()))
res = []
for i in range(0, 2 * t, 2):
    res.append([bin(a[i])[2:], bin(a[i + 1])[2:]])
for k in range(t):
    s = res[k][0]
    t = res[k][1]
    ls = len(res[k][0])
    lt = len(res[k][1])
    g = [[0] * (lt + 1) for _ in range(ls + 1)]
    for i in range(ls + 1):
        g[i][0] = i
    for i in range(lt + 1):
        g[0][i] = i
    for i in range(1, ls + 1):
        for j in range(1, lt + 1):
            left = g[i - 1][j] + 1
            down = g[i][j - 1] + 1
            left_down = g[i - 1][j - 1]
            if s[i - 1] != t[j - 1]:
                left_down += 1
            g[i][j] = min(left, down, left_down)
    print(g[ls][lt])
