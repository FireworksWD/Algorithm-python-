m, n = map(int, input().split())
k = int(input())
bag = []
for i in range(k):
    bag.append(list(map(int, input().split())))
dp = [[float('inf')] * 101 for _ in range(101)]
dp[0][0] = 0
for i in range(k):
    for j in range(m, -1, -1):
        for l in range(n, -1, -1):
            t1 = j + bag[i][0]
            t2 = l + bag[i][1]
            if t1 > m: t1 = m
            if t2 > n: t2 = n
            if dp[t1][t2] > dp[j][l] + bag[i][2]:
                dp[t1][t2] = dp[j][l] + bag[i][2]
print(dp[m][n])
