x,t= map(int,input().split())
z=t//3
if x<=2:
    print(6+z)
elif 2<x<=10:
    s = float((x-2)*1.8 + 6+z)
    if s == int(s):
        print(s)
    else:
        print('%.1f'%s)
else:
    m = (float(8*1.8 + 6)+(x-10)*1.8*1.5+z)
    if m==int(m):
        print(m)
    else:
        print('%.1f'%m)