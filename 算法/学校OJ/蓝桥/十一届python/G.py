a = list(input())
m = a[0]
for i in a:
    if a.count(i) > a.count(m):
        m = i
print(m)
print(a.count(m))
