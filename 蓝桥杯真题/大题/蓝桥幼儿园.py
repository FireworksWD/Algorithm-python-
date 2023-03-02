n, m = map(int, input().split())
fa = list(range(n + 1))


def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]


def merge(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        fa[x] = fa[y]


for i in range(m):
    op, x, y = map(int, input().split())
    if op == 1:
        merge(x, y)
    if op == 2:
        i = find(x)
        j = find(y)
        if i == j:
            print('YES')
        else:
            print('NO')
