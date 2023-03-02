al = list(map(int, input().split()))
n = al[0]
a = []
for i in range(1, len(al), 2):
    a.append([al[i], al[i + 1]])
a.sort(key=lambda x: x[0])
dp = [0] * n
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j][1] < a[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
