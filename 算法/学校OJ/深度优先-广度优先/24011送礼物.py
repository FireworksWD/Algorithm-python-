# w, n = map(int, input().split())
# bag = []
# for i in range(n):
#     bag.append(int(input()))
# dp = [0] * (w + 1)
# for i in range(n):
#     for j in range(w, bag[i] - 1, -1):
#         dp[j] = max(dp[j], dp[j - bag[i]] + bag[i])
# print(dp[w])
w, n = map(int, input().split())
bag = []
for i in range(n):
    bag.append(int(input()))
max_res = float('-inf')
res = 0


def backtrack(t):
    global max_res, res
    if t == n:
        max_res = max(max_res, res)
        return
    if res + bag[t] <= w:
        res += bag[t]
        backtrack(t + 1)
        res -= bag[t]
    backtrack(t + 1)


backtrack(0)
print(max_res)
