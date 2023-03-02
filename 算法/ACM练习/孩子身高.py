r,m,f=map(float,input().split())
s=int(r)
if s==0:
    x=(m*0.923+f)/2
    print('%.3f'%x)
else:
    x=(m+f)/2*1.08
    print('%.3f'%x)