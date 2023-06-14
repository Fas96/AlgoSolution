class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        globalSum = 0

        for i in nums:
            if globalSum < 0:
                globalSum = 0
            globalSum += i
            maxSum = max(globalSum, maxSum)
        return maxSum
        