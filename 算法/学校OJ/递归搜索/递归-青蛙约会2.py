def myojilide(a, b):
    if b == 0:
        return (1, 0, a)
    (x, y, r) = myojilide(b, a % b)
    temp = x
    x = y
    y = temp - int(a / b) * y
    return (x, y, r)
x,y,m,n,l=map(int, input().split())

a=n-m
b=l
c=x-y
if a<0:
    a=-a
    c=-c
p,q,z=myojilide(a,b)
if c%z==0:
    k=b//z
    print(((p*c//z)%k+k)%k)
else:
    print('Impossible')