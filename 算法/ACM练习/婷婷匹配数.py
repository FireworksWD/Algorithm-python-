m,n=map(int,input().split())
def ys(x):
    res=set()
    for i in range(2,x//2+1):
        if x%i==0:
            res.add(i)
    return res
s1=ys(m)
s2=ys(n)
if sum(s1)+1==n and sum(s2)+1==m:
    print('yes')
else:
    print('no')