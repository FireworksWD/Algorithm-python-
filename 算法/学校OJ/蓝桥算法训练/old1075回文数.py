# n = int(input())
# m = input()
n, m = map(str, input().split())
n = int(n)


def add(s, n):
    num = int(s, n) + int(s[::-1], n)
    if n == 16:
        return hex(num)[2:]
    return tran(num, n)


def tran(number, n):
    strings = ''
    while number:
        strings += str(number % n)
        number //= n
    return strings


def solve(x, n):
    for i in range(30):
        if x == x[::-1]:
            return f'STEP={i}'
        x = add(x, n)
    return f'Impossible!'


print(solve(m, n))
