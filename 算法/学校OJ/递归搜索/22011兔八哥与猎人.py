import math

n = int(input())
while n:
    a, b, c, d = map(int, input().split())
    if math.gcd(abs(a - c), abs(b - d)) != 1:
        print(0, end=' ')
    else:
        print(1, end=' ')
    n -= 1
