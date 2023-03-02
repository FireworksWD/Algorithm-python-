s = list(input())
a = list(set(s))
res = []
for i in a:
    if s.count(i) > 0:
        res.append(s.count(i))
print(max(res) - min(res))
