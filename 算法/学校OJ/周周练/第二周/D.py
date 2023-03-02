a1 = list(map(int, input().split()))
n = a1[0]
a = a1[1:]
s = set(a)
res = []
for i in s:
    res.append(a.count(i))
print(max(res))
