n = int(input())
a = []
for i in range(n):
     a.append(list(map(int, input().split())))
dp = [[0 for _ in range(n)]for _ in range(n)]
dp[0][0] = a[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = a[i][j] + dp[i-1][j]
        if i == j:
            dp[i][j] = a[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j-1]+a[i][j], dp[i-1][j]+a[i][j])
if n % 2 == 0:
    print(max(dp[-1][n//2-1], dp[-1][n//2]))
else:
    print(dp[-1][n//2])