x = int(input())
if x<=100000:
    s = float(x*0.1 + x)
    print('%.2f'%s)
elif 100000<x<=200000:
    a = float(100000*0.1+(x-100000)*0.75+x)
    print('%.2f' % a)
elif 200000<x<=400000:
    b = float(x+(x-200000)*0.05)
    print('%.2f' % b)
elif 400000<x<=600000:
    c = float(x+(x-400000)*0.03)
    print('%.2f' % c)
elif 600000<x<=1000000:
    d = float(x+(x-600000)*0.015)
    print('%.2f' % d)
else:
    e = float(x+(x-1000000)*0.01)
    print('%.2f' % e)