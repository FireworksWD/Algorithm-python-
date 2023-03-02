n = int(input())
ans = 0
while n != 1:
    for i in range(2, n + 1):
        if n % i == 0:
            print(i, end=' ')
            ans += 1
            n //= i
            break
print()
print(ans)
