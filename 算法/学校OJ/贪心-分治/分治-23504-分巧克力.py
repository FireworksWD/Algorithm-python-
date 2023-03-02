a1 = list(map(int, input().split()))
n, k = a1[0], a1[1]
s = []
for i in range(2, len(a1), 2):
    s.append([a1[i], a1[i + 1]])
l, r = 1, 10 ** 5
while l < r:
    mid = (l + r + 1) // 2
    res = 0
    for i in range(n):
        res += (s[i][0] // mid) * (s[i][1] // mid)
    if res < k:
        r = mid - 1
    else:
        l = mid
print(l)
