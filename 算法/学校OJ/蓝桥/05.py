n = int(input())
a = []
for i in range(n):
    s = list(map(int, input().split()))
    a.append(s)
b = [k for i in a for k in i[1:]]
d={}
for i in b:
    d[b.count(i)]=i
m = max(d.keys())
n = d.get(m)
print(n, end=' ')
print(m)
