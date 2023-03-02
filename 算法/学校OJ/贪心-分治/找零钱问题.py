n = int(input())
a=list(map(int,input().split()))
x = [1,5,10,50,100,500]
ans = 0
s= 0
for i in range(len(a)):
    s+=a[i]*x[i]
if s<n:
    print(-1)
for i in reversed(range(len(a))):
    t=min(n//x[i],a[i])
    n-=t*x[i]
    ans+=t
print(ans)