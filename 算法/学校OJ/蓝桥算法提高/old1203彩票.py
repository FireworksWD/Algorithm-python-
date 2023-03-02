n = int(input())
a = list(map(int, input().split()))
res = [0] * 8
for i in range(n):
    b = list(map(int, input().split()))
    cnt = 0
    for j in b:
        if a.count(j) > 0:
            cnt += 1
    res[cnt] += 1
for x in range(7, 0, -1):
    print(res[x], end=' ')
