def comp():
    tmp = 0
    for i in range(k):
        if len[i] > tmp:
            tmp = len[i]
    return tmp


def search(dep, len, t):
    global best

    if dep == n:
        tmp = comp()
        if tmp < best:
            best = tmp
        return

    for i in range(k):
        len[i] += t[dep]
        if len[i] < best:
            search(dep + 1, len, t)
        len[i] -= t[dep]


if __name__ == "__main__":
    best = 99999
    a = list(map(int, input().split()))
    n, k = a[0], a[1]
    t = a[2:]
    len = [0 for _ in range(k)]
    x = [0 for _ in range(n)]
    search(0, len, t)
    print(best)
