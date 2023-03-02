'''给定一个长度为 n+1 的数组nums，数组中所有的数均在 1∼n 的范围内，其中 n≥1。
请找出数组中任意一个重复的数，但不能修改输入的数组。
数据范围
1≤n≤1000
样例
给定 nums = [2, 3, 5, 4, 3, 2, 6, 7]。
返回 2 或 3。
思考题：如果只能使用 O(1) 的额外空间，该怎么做呢？'''
nums = list(map(int, input().split()))


# def solve(nums: list):
#     res = [0] * 1001
#     for i in nums:
#         res[i] += 1
#     for i in range(1, 1001):
#         if res[i] > 1:
#             return i
#     return
#
# print(solve(nums))


# 分治
# 按数组里数的大小进行二分而不是数的下标
# 把区间划分为[l,mid],[mid+1,r]
# 统计左半边个数，如果大于区间长度说明有重复元素，将区间更新为[l,mid]，反之更新为[mid+1,r]
def split(nums: list):
    l, r = 1, len(nums) - 1
    while l < r:
        mid = l + r >> 1
        cnt = 0
        for v in nums:
            if l <= v and v <= mid:
                cnt += 1
        if cnt > mid - l + 1:
            r = mid
        else:
            l = mid + 1
    return r


print(split(nums))
# Int是将一个数值向下取整为最接近的整数的函数。Int是数据库中常用函数中的取整函数，常用来判别一个数能否被另一个数整除
# 是比特操作,可以看做是除2，如
# 15的二进制表示是00001111,15>>1将00001111右移一位，变为00000111，即7.
# 另外<<就是左移，相当于乘以2.