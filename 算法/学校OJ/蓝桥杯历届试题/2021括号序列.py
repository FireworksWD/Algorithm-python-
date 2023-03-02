s = input()
n = len(s)
mod = 1000000007
N = n + 5
dp = [[0 for i in range(N)] for j in range(N)]


def calc():
    dp[0][0] = 1
    for i in range(1, n + 1):
        if s[i - 1] == "(":
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] % mod
        else:
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][0]) % mod
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j + 1] + dp[i][j - 1]) % mod
    for i in range(n + 1):
        if dp[n][i] != 0:
            return dp[n][i]
    return -1


left = int(calc())
a = list(s[::-1])
for i in range(n):
    if a[i] == ")":
        a[i] = "("
    else:
        a[i] = ")"
s = ''.join(a)
right = calc()
print((left * right) % mod)
