class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def checkInc(nums):
            for i in range(1, len(nums)):
                if nums[i - 1] >= nums[i]:
                    return False
            return True
        for i in range(len(nums)):
            if (checkInc(nums[:i]+nums[i+1:])):
                return True
        return False
        