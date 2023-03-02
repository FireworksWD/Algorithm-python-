n,m,k=map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
def check(x):
    c=0
    j=m
    for i in range(n):
        while a[i]+b[j-1]>x and j>0:
            j-=1
        if a[i]+b[j]<=x:
            c+=j
    if c>=k:
        return 0
    return 1
l=1
r=2*10**9
while l<=r:
    mid=(1+r+l)//2
    if check(mid):
        l=mid+1
    else:
        r=mid-1
print(l)