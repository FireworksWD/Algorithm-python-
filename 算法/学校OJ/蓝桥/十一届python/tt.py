n = int(input())
def ss(n):
    r = 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    while n > 4:
        r *= 3
        n -= 3
    r *= n
    return r % 5218
print(ss(n))