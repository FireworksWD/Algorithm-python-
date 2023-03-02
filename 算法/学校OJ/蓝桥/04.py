n = int(input())
f1,f2,f3=0,1,1
if n==1:
    print(0)
if n==2:
    print(0,end=' ')
    print(1,end=' ')
if n==3:
    print(0, end=' ')
    print(1, end=' ')
    print(1,end=' ')
if n > 3:
    print(0, end=' ')
    print(1, end=' ')
    print(1, end=' ')
    for i in range(4,n+1):
        f2,f3=f3,f2+f3
        print(f3,end=' ')