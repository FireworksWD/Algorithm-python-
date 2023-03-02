def solve(n):
    p3, p5, p7 = 1, 1, 1
    dp = [0] * (n + 1)
    dp[1], dp[2], dp[3] = 3, 5, 7
    for i in range(4, n + 1):
        num3, num5, num7 = dp[p3] * 3, dp[p5] * 5, dp[p7] * 7
        dp[i] = min(num3, num5, num7)
        if dp[i] == num3: p3 += 1
        if dp[i] == num5: p5 += 1
        if dp[i] == num7: p7 += 1
    return dp


n = int(input())    
x = solve(10**6)
for i in range(10**6):
    if x[i] == n:
        print(i)
        break
