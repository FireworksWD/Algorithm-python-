n=int(input())
test=[list(map(int,input().split())) for i in range(n)]
res=[]
def check(a1,a2,a3):
    if a2-a1==a3-a2:
        return True
    return False
def dc(a1,a2,a3,n):
    x=a1+(n-1)*(a3-a2)
    return x
def db(a1,a2,a3,n):
    q=a3//a2
    x=a1
    for i in range(1,n):
        x*=q%202276
    return x%202276
for i in test:
    if check(i[0],i[1],i[2]):
        r=dc(i[0],i[1],i[2],i[3])
        res.append(r%202276)
    else:
        r=db(i[0],i[1],i[2],i[3])
        res.append(r)
for i in range(n):
    print(res[i])