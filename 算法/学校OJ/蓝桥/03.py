def s(m,k):
    n=m
    a=[]
    c=0
    while n<k:
        l = [i for i in range(2, n) if n % i == 0]
        if not l:
            a.append(n)
        n+=1
    for i in range(len(a)):
        if a[i]-a[i-1]==2:
            c+=1
    print(c)
m,n=map(int,input().split())
s(m,n)