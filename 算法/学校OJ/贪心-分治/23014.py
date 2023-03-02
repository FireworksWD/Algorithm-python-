a1=list(map(int,input().split()))
m,n=a1[0],a1[1]
vals=[]
nums=[]
for i in range(2,len(a1),2):
    vals.append(a1[i])
    nums.append(a1[i+1])
dp=[float('inf')]*(m+1)
dp[0]=0
for i in range(n):
    for j in range(1,nums[i]+1):
        for k in range(m,vals[i]-1,-1):
            dp[k]=min(dp[k],dp[k-vals[i]]+1)
if dp[m]==float('inf'):
    print(-1)
else:
    print(dp[m])