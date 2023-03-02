n, v = map(int, input().split())
bag = []
for i in range(n):
    bag.append(list(map(int, input().split())))
dp = [0] * (v + 1)
for i in range(n):
    if bag[i][2] == 0:
        for j in range(bag[i][0], v + 1):
            dp[j] = max(dp[j], dp[j - bag[i][0]] + bag[i][1])
    else:
        for j in range(v, -1, -1):
            for k in range(bag[i][2]):
                if j - k * bag[i][0] < 0:
                    break
                dp[j] = max(dp[j], dp[j - k * bag[i][0]] + k * bag[i][1])
print(dp[v])
