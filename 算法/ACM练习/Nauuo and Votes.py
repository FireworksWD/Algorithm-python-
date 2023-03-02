x,y,z=map(int,input().split())
if z==0:
    if x==y:
        print(0)
    if x>y:
        print('+')
    if x<y:
        print('-')
else:
    if x>y:
        t=x-y
        if t<=z:
            print('?')
        if t>z:
            print('+')
    if x<y:
        t=y-x
        if t<=z:
            print('?')
        if t>z:
            print('-')
    if x==y:
        print('?')