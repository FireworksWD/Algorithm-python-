n = int(input())
a = [0] * 100001
nubset = set()
ans = 0
for i in range(1, 100001):
    a[i] = i * i
    nubset.add(a[i])
for i in range(1, 100001):
    if a[i] <= n:
        s = str(a[i])
        temp = set()
        su = 0
        for ch in s:
            temp.add(ch)
            su += int(ch)
        if len(temp) == len(s) and su in nubset:
            ans += 1
print(ans)
