m, n = map(int, input().split())
k = int(input())
fa = list(range(m * n + 1))
ans = 0


def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]


def merge(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        fa[x] = fa[y]


for i in range(k):
    x, y = map(int, input().split())
    merge(x, y)
for i in range(1, m * n + 1):
    if fa[i] == i:
        ans += 1
print(ans)
