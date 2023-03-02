n,c=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
p1=0
p2=n-1
t=0
while n>0:
    if a[p1]+a[p2]>c:
        p2-=1
        n-=1
        t+=1
    else:
        p1+=1
        p2-=1
        n-=2
        t+=1
print(t)