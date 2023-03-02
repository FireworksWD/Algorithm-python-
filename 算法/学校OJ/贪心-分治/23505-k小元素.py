a = list(map(int, input().split()))
k = a.pop(1)
a.pop(0)
a.sort()
if k > len(a):
    print(-1)
else:
    print(a[k - 1])
