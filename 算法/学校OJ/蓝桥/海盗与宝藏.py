n,m=map(int,input().split())
p = list(map(int,input().split()))
w = list(map(int,input().split()))
p.insert(0,0)
w.insert(0,0)
dp=[[0 for col in range(m+1)]for raw in range(n+1)]
def dfs(w,p,n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (j>=w[i]):
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+p[i])
            else:
                dp[i][i]=dp[i-1][j]
    v=dp[n][m]
    return v
print(dfs(w,p,n,m))