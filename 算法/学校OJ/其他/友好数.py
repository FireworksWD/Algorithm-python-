a,b=map(int,input().split())
def check(n):
    x=set()
    for i in range(2,n//2+1):
        if n%i==0:
            x.add(i)
    return sum(list(x))+1
if check(a)==b and check(b)==a:
    print('yes')
else:print('no')