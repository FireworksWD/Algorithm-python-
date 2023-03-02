n, k, s = list(map(int, input().split()))
lens = len(str(s))
s = '0' + str(s)
number = [[0] * 45 for _a in range(45)]  # i-j的数字
dp = [[0] * 45 for _ in range(45)]  # 1-i分割j个*号
for i in range(1, lens + 1):
    for j in range(i, lens + 1):
        for l in range(i, j + 1):
            number[i][j] = int(s[i:j + 1])
    dp[i][0] = int(s[1:i + 1])  # 0个*号时是本身
for j in range(1, k + 1):  # 分割1-k个*号
    for i in range(1, lens + 1):  # 枚举终点
        for l in range(1, i):  # 分割点插入个乘号
            dp[i][j] = max(dp[i][j], dp[l][j - 1] * number[l + 1][i])
print(dp[lens][k])
