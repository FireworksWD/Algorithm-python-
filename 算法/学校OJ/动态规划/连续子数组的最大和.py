class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre=0
        maxres=nums[0]
        for i in range(len(nums)):
           pre=max(pre+nums[i],nums[i])
           maxres=max(pre,maxres)
        return maxres