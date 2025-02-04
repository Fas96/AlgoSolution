class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mx=nums[0]
        curmax=mx

        n=len(nums)
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                curmax+=nums[i]
            else:
                curmax=nums[i]
            mx=max(curmax,mx)
        return mx
        