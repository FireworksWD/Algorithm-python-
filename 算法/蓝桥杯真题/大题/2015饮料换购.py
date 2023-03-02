n = int(input())
ans = n
while n >= 3:
    ans += n // 3
    n = n % 3 + n // 3
print(ans)
