n,m=map(int,input().split())
dp=[[0]*40 for _ in range(40)]
dp[0][1]=1
for i in range(1,m+1):
    for j in range(1,n+1):
        a=j-1
        if a==0:a=n
        b=j+1
        if b==n+1:b=1
        dp[i][j]=dp[i-1][a]+dp[i-1][b]
print(dp[m][1])