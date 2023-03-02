n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
dp = [[0 for _ in range(n)]for _ in range(n)]
dp[0][0]=arr[0][0]
for i in range(n):
    for j in range(n):
        dp[i][j]=max(dp[i][j]+arr[i-1][j], dp[i][j]+arr[i][j-1])
print(dp)