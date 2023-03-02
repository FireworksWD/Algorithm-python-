n=int(input())
res=set()
for i in range(2,n):
    if n%i==0:
        res.add(i)
print(len(res)+1)