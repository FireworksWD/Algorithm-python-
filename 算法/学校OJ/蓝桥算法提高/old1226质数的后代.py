def check(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


res = []
n = int(input())
for i in range(n):
    y = int(input())
    f = False
    for v in range(2, y // 2 + 1):
        if check(v):
            if y % v == 0 and check(y // v):
                res.append('Yes')
                f = True
                break
    if not f:
        res.append('No')
for i in res:
    print(i)
