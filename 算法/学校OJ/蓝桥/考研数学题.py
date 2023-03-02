x,n=map(int,input().split())
def fact(n):
    x=1
    for i in range(1,n+1):
        x*=i
    return x
def mypow(x,n):
    return x**n
s=0
for i in range(1,n+1):
    a = round((-1)**(i-1)*fact(x) / mypow(x, i),4)
    s+=a
print(round(s,4))