n = int(input())
a = []
a.append('A')
for i in range(1, n):
    length = len(a)
    a.append(chr(ord('A') + i))
    for j in range(length):
        a.append(a[j])
for i in range(2**n - 1):
    print(a[i], end='')
print()