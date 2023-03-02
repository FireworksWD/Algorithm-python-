al1 = list(map(int, input().split()))
n, m = al1[0], al1[1]
al = al1[2:]
al.sort(reverse=True)
res = 0
temp = 0
if sum(al)<m:
    print(-1)
else:
    for i in range(n):
        temp += al[i]
        if temp <= m:
            res += 1
        else:
            break
    print(res)
