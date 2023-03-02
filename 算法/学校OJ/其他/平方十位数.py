import itertools
s=[i for i in range(10)]
res=0
for i in itertools.permutations(s,10):
    x=[str(k) for k in i]
    temp=int(''.join(x))
    if temp**0.5==int(temp**0.5) and len(str(temp))==10:
        res+=1
print(res)