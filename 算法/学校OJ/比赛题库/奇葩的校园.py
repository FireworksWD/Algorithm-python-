n=int(input())
vis=[0]*31
vis[1]=1
ans=0
def dfs(k):
    global ans
    if k==n:
        ans+=1
        return
    for i in range(2,n+1):
        if vis[i]:continue
        if i==k:continue
        if i%k==0 or k%i==0:
            vis[k]=1
            dfs(i)
            vis[k]=0
dfs(1)
print(ans)