x,y,z=map(int,input().split())
a=[0]*101
b=[0]*101
for i in range(1,x+1):
    a[i]=1
    b[i]=0
for j in range(x+1,z+2):
    b[j]=y*a[j-x]
    a[j]=a[j-1]+b[j-2]
print(a[z+1])