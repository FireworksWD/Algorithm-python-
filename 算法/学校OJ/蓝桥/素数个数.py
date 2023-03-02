def s(n):
    a=[True]*n
    b=[]
    for i in range(2,n):
        if a[i]:
            b.append(i)
        for k in b:
            l = i*k
            if l>=n:
                break
            a[l]=False
            if i%k==0:
                break
    c=0
    for i in range(len(b)):
        for j in range(len(b)-1,i,-1):
            if b[i]+b[j]<=n-1:
                c+=j-i+1
                break
    print(c)
n = int(input())
s(n+1)

