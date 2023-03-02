lis1 = list(map(int, input().split()))
lis = lis1[1:]
n = lis1[0]
res = 0
for i in range(n):
    for j in range(i):
        if lis[j] > lis[i]:
            res += 1
print(res)
