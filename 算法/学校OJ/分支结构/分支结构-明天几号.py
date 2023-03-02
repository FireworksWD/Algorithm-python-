a,b,c=map(int,input().split())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    if b==1 or b==3 or b==5 or b==7 or b==8 or b==10:
        if c==31:
            print(a, end=' ')
            print(b+1,end=' ')
            print(1)
        else:
            print(a, end=' ')
            print(b, end=' ')
            print(c+1)
    elif b==2:
        if c==29:
            print(a, end=' ')
            print(b + 1, end=' ')
            print(1)
        else:
            print(a, end=' ')
            print(b, end=' ')
            print(c + 1)
    elif b==4 or b==6 or b==9 or b==11:
        if c==30:
            print(a, end=' ')
            print(b + 1, end=' ')
            print(1)
        else:
            print(a, end=' ')
            print(b, end=' ')
            print(c + 1)
    elif b==12:
        if c==31:
            print(a+1, end=' ')
            print(1, end=' ')
            print(1)
else:
    if b==1 or b==3 or b==5 or b==7 or b==8 or b==10:
        if c==31:
            print(a, end=' ')
            print(b+1,end=' ')
            print(1)
        else:
            print(a, end=' ')
            print(b, end=' ')
            print(c+1)
    elif b==2:
        if c==28:
            print(a, end=' ')
            print(b + 1, end=' ')
            print(1)
        else:
            print(a, end=' ')
            print(b, end=' ')
            print(c + 1)
    elif b==4 or b==6 or b==9 or b==11:
        if c==30:
            print(a, end=' ')
            print(b + 1, end=' ')
            print(1)
        else:
            print(a, end=' ')
            print(b, end=' ')
            print(c + 1)
    elif b==12:
        if c==31:
            print(a+1, end=' ')
            print(1, end=' ')
            print(1)