n, m = map(int, input().split())
bag = []
for i in range(n):
    x, y, z = map(int, input().split())
    bag.append([x, y, z])
dp = [0] * (m + 1)
for i in range(n):
    for j in range(m, -1, -1):
        for k in range(bag[i][2] + 1):
            if j - k * bag[i][0] < 0:
                break
            dp[j] = max(dp[j], dp[j - k * bag[i][0]] + k * bag[i][1])
print(dp[m])
