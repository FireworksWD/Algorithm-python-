a1 = list(map(int, input().split()))
a = a1[1:]
avg = sum(a) // len(a)
res = 0
temp = 0
for i in range(a1[0]):
    temp += a[i] - avg
    if temp != 0:
        res += 1
print(res)
