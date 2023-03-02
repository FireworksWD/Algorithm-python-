n = int(input())
z = []
for i in range(n):
    a = list(map(int,input().split()))
    b = a[:3]
    c = a[3:]
    x = max(b)
    y = max(c)
    if x>y:
        b.remove(x)
        if y>b[0] and y>b[1]:
            z.append('YSE')
        else:
            z.append('NO')
    if x<y:
        c.remove(y)
        if x>c[0] and x>c[1]:
            z.append('YES')
        else:
            z.append('NO')
for i in z:
    print(i)