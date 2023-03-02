n = int(input())
res = []
for i in range(n):
    name, d, source = map(str, input().split())
    res.append([name, d, int(source)])
res.sort(key=lambda x: x[2])
print(*res[-1][:2])
print(*res[0][:2])
