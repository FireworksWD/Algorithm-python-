import itertools
s = [i for i in range(1, 11)]
res = []
for k in itertools.permutations(s, 10):
    dp = [[0] * 10 for i in range(10)]
    x = list(k)
    for j in range(10):
        dp[-1][j] = x[j]
    for i in range(8,-1,-1):
        for j in range(i+1):
            if i==8 and j==4:
                dp[i][j]=0
            else:
                dp[i][j]=dp[i+1][j+1]+dp[i+1][j]
    res.append(dp[0][0])
print(f'最小的数字:{min(res)}')
