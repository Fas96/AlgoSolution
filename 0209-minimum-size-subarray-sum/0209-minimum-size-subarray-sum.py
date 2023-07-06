class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = float('inf')
        left = 0
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            while curSum >= target:
                res = min(res, i - left + 1)
                curSum -= nums[left]
                left += 1
        return res if res != float('inf') else 0
        