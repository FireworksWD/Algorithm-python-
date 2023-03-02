class stra:
    def __init__(self, a, b):
        self.a = a
        self.b = b
def rel(l1, l2):
    if l1.a == l2.a:
        return
    x = -(l1.b-l2.b)/(l1.a-l2.a)
    y = l1.a*x+l1.b
    point.add((x, y))
n = int(input())
l = []
for i in range(n):
    a, b = list(map(int, input().split()))
    l.append(stra(a, b))
res = 0
if l:
    res = 2
    for i in range(1, len(l)):
        point = set()
        for j in range(i):
            rel(l[i], l[j])
        res += len(point) + 1
print(res)