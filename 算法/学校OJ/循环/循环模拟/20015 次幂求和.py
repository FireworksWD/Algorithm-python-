n, k = map(int, input().split())
ans = 0
a = [0] * 10007
b = [0] * 10007
x = n % 10007
for i in range(10007):
    if x >= i:
        a[i] = n // 10007 + 1
    else:
        a[i] = n // 10007
for j in range(10007):
    b[j] = 1
for j in range(1, k + 1):
    for i in range(10007):
        b[i] = b[i] * i % 10007
for i in range(10007):
    ans = (ans + a[i] * b[i]) % 10007
print(ans)
