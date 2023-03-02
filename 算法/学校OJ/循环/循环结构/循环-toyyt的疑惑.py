def s(n):
    a=[True]*1345678
    b=[]
    for i in range(2,1345678):
        if a[i]:
            b.append(i)
        for j in b:
            l=i*j
            if l>=1345678:
                break
            a[l]=False
            if i%j==0:
                break
        if len(b)==n:
            break
    return b
n = int(input())
b=s(n)
s=1
for i in b:
    s*=i%50000
print(s%50000)