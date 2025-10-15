class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev, increaseCount = 0, 1
        maxK=0

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                increaseCount += 1
            else:
                maxK=max(maxK,increaseCount // 2,min(increaseCount, prev))
                prev = increaseCount
                increaseCount = 1
        return max(maxK,increaseCount // 2,min(increaseCount, prev))