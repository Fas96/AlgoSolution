class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        globalMax = 0

        for n in nums:
            globalMax += n
            maxSub = max(maxSub, globalMax)
            globalMax = max(globalMax, 0)
        return maxSub