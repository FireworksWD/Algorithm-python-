n,m=map(int,input().split())
value=list(map(int,input().split()))
value.sort()
res,c=0,m
for i in range(n):
    t=m//value[i]
    c-=t*value[i]
    res+=t
    if c==0:
        print(res)
        break
    if c<0:
        print(-1)
        break