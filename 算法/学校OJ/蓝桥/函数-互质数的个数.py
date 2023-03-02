def f(n):
    j = 0
    for i in range(2, n):
        a = n
        q = i
        r = a % i
        while r != 1 and r != 0:
            a = int(q)
            q = int(r)
            r = int(a) % int(q)
        if r == 1:
            j += 1
    print(j)
n = int(input())
f(n)
