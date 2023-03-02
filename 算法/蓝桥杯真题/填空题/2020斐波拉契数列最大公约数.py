import math


def fib(n):
    f1, f2 = 1, 1
    for i in range(3, n + 1):
        c = f1 + f2
        f1, f2 = f2, c
    return f2


print(math.gcd(fib(2020), fib(520)))
