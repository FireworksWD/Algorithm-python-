n = int(input())
if n == 1: print(0)
if n % 2 == 0:
    print(1)
else:
    print(-1)
# def fib(x):
#     if x == 1 or x == 2:
#         return 1
#     f1, f2 = 1, 1
#     for i in range(3, x + 1):
#         c = f1 + f2
#         f1, f2 = f2, c
#     return f2
#
#
# print(fib(n - 1) * fib(n + 1) - fib(n) ** 2)
