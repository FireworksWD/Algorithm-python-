n = int(input())
a = list(map(int, input().split()))
b = 0
for i in range(len(a)):
    if len(a) >= 2:
        a.sort()
        c = a[0] + a[1]
        b += c
        del (a[0], a[0])
        a.append(c)
    if len(a) == 1:
        print(b)
        break