n=int(input())
a_list=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]
dp[0][0]=a_list[0][0]
for i in range(1,n):
    for j in range(i+1):
        if j==0:dp[i][j]=dp[i-1][j]+a_list[i][j]
        elif i==j:dp[i][j]=dp[i-1][j-1]+a_list[i][j]
        else:dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+a_list[i][j]
print(max(dp[-1]))