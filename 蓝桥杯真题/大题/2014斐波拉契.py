n, m, p = map(int, input().split())


def fib(x):
    if x == 1:
        return x, x
    if x == 2:
        return 2, 1
    a, b = 1, 1
    ans = 2
    for i in range(3, x + 1):
        c = a + b
        ans += c
        a, b = b, c
    return ans, b


x1, x2 = fib(n)
y1, y2 = fib(m)
print(x1 % y2 % p)
