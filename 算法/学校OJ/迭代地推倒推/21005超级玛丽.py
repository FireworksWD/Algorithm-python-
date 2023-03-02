al = list(map(int, input().split()))
n, m = al[0], al[1]
a = [0] * 101
b = [0] * 101
b[1] = 1
for i in range(2, len(al)):
    a[al[i]] += 1
for i in range(2, n + 1):
    if a[i]:
        b[i] = 0
    else:
        b[i] = b[i - 1] + b[i - 2]
print(b[n])
