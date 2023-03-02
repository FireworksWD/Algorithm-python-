p=[]
n=int(input())
def digt(n,a):
    if n!=0:
        digt(n//10,a)
        t=n%10
        z=t**3
        a.append(z)
    return a
if n>1000:
    print(5)
else:
    for i in range(1, n+1):
        m = []
        digt(i, m)
        if sum(m) == i:
            p.append(i)
    print(len(p))


