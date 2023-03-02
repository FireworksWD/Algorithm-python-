a1 = list(map(int, input().split()))
n, r = a1[0], a1[1]
a = a1[2:]
s = [0] * (r + 1)
j, min_x = 0, 0
a.sort()
for i in range(n):
    j += 1
    if j == r + 1:
        j = 1
    s[j] += a[i]
    min_x += s[j]
print(min_x)
