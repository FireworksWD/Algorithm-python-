import bisect

# 蓝桥骑士 dp lis(Longest Increasing Subsequence)
n = int(input())
alist = list(map(int, input().split()))
dp = []
for i in alist:
    if not dp or i > dp[-1]:
        dp.append(i)
    else:
        index = bisect.bisect_left(dp, i)
        dp[index] = i
print(len(dp))
