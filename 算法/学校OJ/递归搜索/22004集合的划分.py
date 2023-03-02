n, k = map(int, input().split())
dp = [0] * 1005
for i in range(1, n + 1):
    dp[i] = 1
for i in range(2, n + 1):
    for j in range(i - 1, 1, -1):
        dp[j] = dp[j - 1] + j * dp[j]
print(dp[k])


# def solve(n, k):
#     if k == 0 or n < k:
#         return 0
#     if k == n or k == 1:
#         return 1
#     return solve(n - 1, k - 1) + k * solve(n - 1, k)
#
#
# print(solve(n, k))
