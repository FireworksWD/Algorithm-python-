# n, v = map(int, input().split())
# bag = []
# for i in range(n):
#     bag.append(list(map(int, input().split())))
# dp = [0] * (v + 1)
# for i in range(n):
#     for j in range(v, -1, -1):
#         for k in range(bag[i][2] + 1):
#             if bag[i][0] * k <= j:
#                 dp[j] = max(dp[j], dp[j - bag[i][0] * k] + bag[i][1] * k)
# print(dp[v])
n, m = map(int, input().split())
f = [0] * 2010
bag = []
for i in range(n):
    w, v, s = map(int, input().split())
    k = 1
    while k <= s:
        bag.append([w * k, v * k])
        s -= k
        k <<= 1
    if s > 0:
        bag.append([w * s, v * s])
for good in bag:
    for j in range(m, good[0] - 1, -1):
        f[j] = max(f[j], f[j - good[0]] + good[1])
print(f[m])
