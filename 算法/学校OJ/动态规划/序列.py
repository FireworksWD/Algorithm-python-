n=int(input())
H = list(map(int,input().split()))
maxVal,minVal = 0,0
dp = [0 for _ in range(n)]
#最长不上升序列问题  (最多能拦截导弹数)
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if H[i]<=H[j] and dp[i]<(dp[j]+1):
            dp[i] = dp[j] + 1
    if maxVal < dp[i]:
        maxVal=dp[i]
#最长不下降序列问题  （最少需要几套装备）
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if H[i] > H[j] and dp[i]<(dp[j]+1):
            dp[i] = dp[j] + 1
    if minVal < dp[i]:
        minVal = dp[i]
print(maxVal)
print(minVal)