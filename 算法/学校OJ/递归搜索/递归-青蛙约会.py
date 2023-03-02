x,y,m,n,l=map(int, input().split())
if m==n:
    print('Impossible')
else:
    if m>n:
        c=m-n
        z=(y-x+l)%l
    else:
        c=n-m
        z=(x-y+l)%l
    w=z%c
    r=z//c
    while True:
        if z%c==0:
            print(r)
            break
        else:
            p=z%c+l
            r+=p//c
            z=p%c
        if z==w:
            print('Impossible')