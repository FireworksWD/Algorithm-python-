n = int(input())
a=list(map(int,input().split()))
b=[]
len=0
for i in range(n):
    l=0
    r=0
    while l<r:
        m=l+r+1
        if b[m]<a[i]:
            l=m
        else:
            r=m-1
    len=max(len,r+1)
    b[r+1]=a[i]
print(len)