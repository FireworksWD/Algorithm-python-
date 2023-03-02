a = int(input())
bag = [1, 5, 10, 50, 100, 500]
lis = list(map(int, input().split()))
res = 0
su = 0
for i in range(6):
    su += bag[i] * lis[i]
if su < a:
    print(-1)
else:
    for i in range(5, -1, -1):
        t = min(a // bag[i], lis[i])
        res += t
        a -= t * bag[i]
        if a == 0:
            break
    print(res)
