# n = int(input())
# dp = [0] * (n + 1)
# dp[1] = 1
# p2 = p3 = p5 = 1
# for i in range(2, n + 1):
#     num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
#     dp[i] = min(num2, num3, num5)
#     if dp[i] == num2: p2 += 1
#     if dp[i] == num3: p3 += 1
#     if dp[i] == num5: p5 += 1
# print(dp[n])

# 丑数
def solve(n):
    p2 = p3 = p5 = 1
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
        dp[i] = min(num2, num3, num5)
        if dp[i] == num2: p2 += 1
        if dp[i] == num3: p3 += 1
        if dp[i] == num5: p5 += 1
    return dp[n]


print(f'The 1500\'th ugly number is {solve(1500)}.')