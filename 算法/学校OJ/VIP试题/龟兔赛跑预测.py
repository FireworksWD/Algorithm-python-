v1,v2,t,s,l = map(int,input().split())
if v1<=100 and v2<=100 and t<=300 and s<=10 and l<=10000 and l%v1==0 and l%v2==0:
    s1,s2,i = 0,0,0
    while s1<l and s2<l:
        s1,s2,i=v1+s1,v2+s2,i+1
        if s1==l or s2==l:
            break
        elif s1-s2>=t:
            s2,i=s2+v2*s,i+s
    if s1>s2:print('R')
    if s1==s2:print('D')
    if s1<s2:print('T')
    print(i)
