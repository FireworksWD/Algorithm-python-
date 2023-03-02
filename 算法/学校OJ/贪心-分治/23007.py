a1=list(map(int,input().split()))
n=a1[0]
money=a1[1:]
money.sort(reverse=True)
ans=0
if sum(money)<n:
    print(-1)
else:
    for i in range(n):
        t=n//money[i]
        