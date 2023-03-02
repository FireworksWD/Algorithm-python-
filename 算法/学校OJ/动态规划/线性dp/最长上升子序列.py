import time

n = input()
nums = list(map(int, input().split()))


def solve(nums: list):
    dp, res = [0] * len(nums), 0
    for num in nums:
        i, j = 0, res
        while i < j:
            mid = i + j >> 1
            if dp[mid] < num:
                i = mid + 1
            else:
                j = mid
        dp[i] = num
        if j == res: res += 1
    return res


start = time.time()
print(solve(nums))
end = time.time()
print(end - start)


def slove2(nums: list):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


s1 = time.time()
print(slove2(nums))
e1 = time.time()
print(e1 - s1)
