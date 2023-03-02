n,k,T=map(int,input().split())
sum=t=a=1
for i in range(1,T):
    t=(((a+a+n-1)*n//2)+t)%k
    sum+=t
    a+=n
print(sum)