n, k = map(int, input().split())
nums = list(map(int, input().split()))
index = res = 0
while index <= n - k:
    temp = min(nums[index:index + k])
    if temp != 0:
        res += temp
        for t in range(index, index + k):
            nums[t] -= temp
    for l in range(index, index + k):
        if nums[l] == 0:
            index = l
    index += 1
print(res + sum(nums))
