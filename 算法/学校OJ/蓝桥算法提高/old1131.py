n = int(input())
i = int(input())
j = int(input())
for x in range(1, n + 1):
    print((i, x), end=' ')
print()
for y in range(1, n + 1):
    print((y, j), end=' ')
print()
for x in range(1, n + 1):
    if x - i + j <= n and x - i + j > 0:
        print((x, x - i + j), end=' ')
print()
for y in range(1, n + 1):
    if i + j - y <= n and i + j - y > 0:
        print((i + j - y, y), end=' ')
print()
