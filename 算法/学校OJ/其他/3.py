alis = list(map(int, input().split()))
n, w = alis[0], alis[1]
vi = alis[2:n + 2]
wi = alis[n + 2:]
dp = [0] * (w + 1)
for i in range(n):
    for j in range(w, wi[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - wi[i]] + vi[i])
print(dp[-1])
