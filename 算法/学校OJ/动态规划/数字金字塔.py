n = int(input())
s = []
for i in range(n):
    s.append(list(map(int,input().split())))

dp = [[0 for i in range(n)]for j in range(n)]
dp[0][0] = s[0][0]
for i in range(n):
    for j in range(i+1):
        dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])+s[i][j]

print(max(dp[n-1]))