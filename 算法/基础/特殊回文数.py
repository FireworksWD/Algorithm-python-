n = int(input())
if 1 <= n <= 54:
    for i in range(10000, 1000000):
        a = str(i)
        b = 0
        if a == a[::-1]:
            for j in a:
                b += int(j)
                if b == n:
                    print(a)