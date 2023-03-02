def f(n,m):
    x=0
    y=0
    z=0
    c=0
    v=0
    for i in range(1,n+1):
        if len(str(i))==1:
            if i==m:
                x+=1
        elif len(str(i))==2:
            a,b=map(int,str(i))
            if a+b==m:
                y+=1
        elif len(str(i))==3:
            a,b,c=map(int,str(i))
            if a+b+c==m:
                c+=1
        elif len(str(i))==4:
            a,b,c,d=map(int,str(i))
            if a+b+c+d==m:
                z+=1
        elif len(str(i))==5:
            a,b,c,d,e=map(int,str(i))
            if a+b+c+d+e==m:
                v+=1
    return x+y+z+c+v
n,m=map(int,input().split())
print(f(n,m))