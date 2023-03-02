def f(n):
    res = []
    for x in range(24, 0, -1):  # 因为2的24次方大于10的7次方
        if n >= 2 ** x:
            n -= 2 ** x
            res.append(2 ** x)
    if n == 0:
        print(*res)
    else:
        print(-1)


f(n=int(input()))
