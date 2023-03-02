n,m=map(int,input().split())
a=list(map(int,input().split()))
if m==0:
    print(max(a)-min(a))
else:
    t=a
    t1=max(a)
    t2=min(a)
