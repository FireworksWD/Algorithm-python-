'''m=int(input())
n=int(input())
s=[]
for i in range(n):
    s.append(list(map(int,input().split())))
dp=[[0]*n for i in range(n)]
dp[0][0]=s[0][0]
for i in range(n):
    for j in range(i+1):
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+s[i][j]
print(max(dp[n-1]))'''
T = int(input())
for i in range(T):
    n = int(input())
    dp = []
    #定义一个二维列表
    for i in range(n):
        #输入路径上的数据
        t = list(map(int,input().split()))
        dp.append(t)
    for i in range(n-2,-1,-1):
        #n-2表示从第二行开始往上推
        for j in range(i+1):
            #列坐标不得超过当前的行坐标
            dp[i][j] += max(dp[i+1][j],dp[i+1][j+1])
            #当前的值等于正下(dp[i+1][j])和右下(dp[i+1][j+1])的最大数加上他本身
    print(dp[0][0])