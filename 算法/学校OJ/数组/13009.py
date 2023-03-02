a = [0] * 100001
s = list(map(int, input().split()))
s.pop(0)
for i in s:
    a[i] += 1
for j in range(100000):
    if a[j]:
        print(j, end=" ")
