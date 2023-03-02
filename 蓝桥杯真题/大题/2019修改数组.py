n = int(input())
a = list(map(int, input().split()))
fa = [i for i in range(10 ** 6 + 1)]


def find(x):
    global fa
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]


for i in range(n):
    a[i] = find(a[i])
    fa[a[i]] = find(a[i] + 1)
print(*a)
