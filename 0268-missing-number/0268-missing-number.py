class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for idx in range(len(nums)):
            if nums[idx] - (idx+1) == 0:
                return idx 
        return nums[len(nums) - 1] + 1
        