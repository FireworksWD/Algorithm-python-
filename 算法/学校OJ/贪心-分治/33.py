def s(n):
    a=[True]*100000
    b=[]
    for i in range(2,100000):
        if a[i]:
            b.append(i)
        for k in b:
            l = i*k
            if l>=100000:
                break
            a[l]=False
            if i%k==0:
                break
    ans=0
    for k in range(0,len(b)):
        c=0
        for j in range(k,len(b)):
            if b[j]+c<n:
                c+=b[j]
            elif b[j]+c==n:
                ans+=1
            else:
                break
    print(ans)
n = int(input())
s(n)