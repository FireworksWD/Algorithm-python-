n = int(input())
b = [0] * 10 ** 5
c = [list(map(int, input().split())) for i in range(n)]
a = []
for i in c:
    for j in i:
        a.append(j)
a.sort()
m, q = 0, 0
for i in range(len(a)):
    b[a[i]] += 1
for i in range(a[0], a[-1] + 1):
    if b[i] == 0:
        m = i
    if b[i] == 2:
        q = i
print(m, q)
