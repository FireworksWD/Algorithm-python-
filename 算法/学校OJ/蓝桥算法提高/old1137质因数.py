n = int(input())
print(n, end='=')
while n > 1:
    for i in range(2, n+1):
        if n % i == 0:
            n //= i
            if n == 1:
                print(i)
            if n != 1:
                print(i, end='*')
            break
