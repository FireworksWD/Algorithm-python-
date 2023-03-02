al = list(map(int, input().split()))
n, m = al[0], al[1]
a = al[2:]
l, r = 0, 2 * 10 ** 9
while l < r:
    mid = (l + r + 1) // 2
    count = 0
    for i in range(n):
        count += a[i] // mid
    if count < m:
        r = mid - 1
    else:
        l = mid
print(l)
