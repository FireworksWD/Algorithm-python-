m, n = map(int, input().split())
if m < n:
    Min = m
else:
    Min = n
s = int(Min/2 + 0.5)
ls = [[] for i in range(m)]
for i in range(m):
    line = input().split()
    for j in range(n):
        ls[i].append(line[j])
for k in range(s):
    for i in range(m):
        print(ls[i][0], end=' ')
    for j in range(1, n):
        print(ls[m-1][j], end=' ')
    if m - 2 < 0 or n - 2 < 0:
        break
    for i in range(m-2, -1, -1):
        print(ls[i][n-1], end=' ')
    for j in range(n-2, 0, -1):
        print(ls[0][j], end=' ')
    m = m-2
    n = n-2
    ls2 = [[] for i in range(m)]
    for i in range(m):
        for j in range(n):
            ls2[i].append(ls[i+1][j+1])
    ls = ls2