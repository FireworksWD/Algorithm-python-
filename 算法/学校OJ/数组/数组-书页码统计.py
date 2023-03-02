n, m = map(int, input().split())
a = [0] * 10
for i in range(1, n + 1):
    j = i
    while j:
        a[j % 10] += 1
        j //= 10
print(a[m])
