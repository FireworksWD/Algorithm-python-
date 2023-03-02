import math
a,b,c=map(int,input().split())
def ll(x,y,z):
    gcd=math.gcd(x,y)
    lcm=(x*y)//gcd
    gcd=math.gcd(lcm,z)
    lcm=(lcm*z)//gcd
    return lcm
print(ll(a,b,c))