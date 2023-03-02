# n = int(input())
# bag = []
# for i in range(n):
#     bag.append(list(map(int, input().split())))
# dp = [[0] * n for _ in range(n)]
# dp[0][0] = bag[0][0]
# for i in range(1, n):
#     for j in range(i+1):
#         if j == 0:
#             dp[i][j] = dp[i - 1][j] + bag[i][j]
#         if i == j:
#             dp[i][j] = dp[i - 1][j - 1] + bag[i][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])+bag[i][j]
# print(max(dp[-1]))

n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))
for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        dp[i][j] = max(dp[i + 1][j + 1], dp[i + 1][j]) + dp[i][j]
print(dp[0][0])
