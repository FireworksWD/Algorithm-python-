# n = int(input())
# nums = list(map(int, input().split()))
# dp = [0] * n
# for i in range(n):
#     dp[i] = 1
#     for j in range(i):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# x = max(dp)
# index = dp.index(x)
# lis = [0] * x
# x -= 1
# lis[x] = nums[index]
# for i in range(index, -1, -1):
#     if nums[i] < nums[index] and dp[i] == dp[index] - 1:
#         x -= 1
#         lis[x] = nums[i]
#         index = i
# print('max=' + str(max(dp)))
# for i in lis:
#     print(i, end=' ')


def lis(arr):
    n = len(arr)
    m = [0] * n
    for x in range(n - 2, -1, -1):
        for y in range(n - 1, x, -1):
            if arr[x] < arr[y] and m[x] <= m[y]:
                m[x] += 1
        max_value = max(m)
        result = []
        for i in range(n):
            if m[i] == max_value:
                result.append(arr[i])
                max_value -= 1
    return result


a1 = list(map(int, input().split()))
arr = a1[1:]
res = lis(arr)
print(len(res), end=' ')
for i in res:
    print(i, end=' ')
