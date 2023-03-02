n,c=map(int,input().split())
w = list(map(int,input().split()))
w.sort()
ans=0
s=0
for i in range(n):
    if s+w[i]<c:
        s+=w[i]
        ans+=1
print(ans)