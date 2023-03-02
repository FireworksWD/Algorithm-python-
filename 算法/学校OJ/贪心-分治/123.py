'''n,m=map(int,input().split())
mid=0
a=list(map(int,input().split()))
l=1
r=2*10**9
while l<r:
    mid=(l+r+1)//2
    c=0
    for i in range(n):
        c+=a[i]//mid
    if c<m:
        r=mid-1
    else:
        l=mid
print(l)'''
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
f=[]
for i in range(1,n+1):
    for j in range(a[i],m):
        f[j]+=f[j-a[i]]
print(f[m])