a = list(map(int, input().split()))
n = a[0]
a.pop(0)
s = sum(a)
ave = s // n
cot = 0
for i in range(n):
    if a[i] != ave:
        a[i + 1] += (a[i] - ave)
        cot += 1
print(cot)