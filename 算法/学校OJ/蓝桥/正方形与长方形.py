n,m=map(int,input().split())
if n<m:
    a=n
else:
    a=m
x = ((1+m)*(1+n)*n*m)//4
y = 0
for i in range(1,a+1):
    y += (m-i+1)*(n-i+1)
print(y, end=' ')
print(x-y)