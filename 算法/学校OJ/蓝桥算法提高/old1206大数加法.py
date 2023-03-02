x = [int(i) for i in input()]
y = [int(i) for i in input()]
a=b=[0]*10002
for i in range(len(x)):
    a[i]=x[i]
for j in range(len(y)):
    b[j]=y[j]
print(a,b)
c = [0] * 10001
i, j = len(a) - 1, len(b) - 1
k, x = 0, 0
while k <= i or k <= j:
    c[k] = a[k] + b[k] + x
    x = c[k] // 10
    c[k] %= 10
    k += 1
c[k] = x
if c[k] == 0: k -= 1
for i in range(k, -1, -1):
    print(c[i], end='')
