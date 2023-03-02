a1 = [int(i) for i in input().split()]
n, k = a1[0],a1[1]
a=a1[2:]
a.sort(reverse=True)
limt = n - 1
ans = 0
i = 0
while i < limt - 2:
    l = i + 1
    r = i + 2
    while l < limt:
        while r < limt:
            if (a[i] + a[r] + a[l]) % k == 0:
                ans = max(ans, a[i] + a[r] + a[l])
                limt = r
                l += 1
                r = l + 1
            else:
                r += 1
        l += 1
        r = l + 1
    i += 1
print(ans)
