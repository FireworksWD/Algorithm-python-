n = int(input())


def solve(n):
    if n == 0:
        return
    solve(n // 10)
    print(n % 10, end=' ')


solve(n)
