# n = int(input())
# a = [0] + list(map(int, input().split()))
a = list(map(int, input().split()))
n = a[0]
sums = [0] * 1001
dp = [[float('inf')] * 1001 for i in range(1001)]
for i in range(1, n + 1):
    sums[i] = sums[i - 1] + a[i]
    dp[i][i] = 0
for le in range(2, n + 1):
    i = 1
    while i + le - 1 <= n:
        j = i + le - 1
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + sums[j] - sums[i - 1])
        i += 1
print(dp[1][n])
# n = int(input())
# a = [0] + list(map(int, input().split()))
# s = [0] * 1001
# dp = [[float('inf')] * 1001 for _ in range(1001)]
# for i in range(1, n + 1):
#     s[i] = s[i - 1] + a[i]
#     dp[i][i] = 0
# for l in range(2, n + 1):
#     for i in range(1, n + 2 - l):
#         j = l + i - 1
#         for k in range(i, j):
#             dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + s[j] - s[i - 1])
# print(dp[1][n])
