class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0
        
        for num in nums:
            if num != 0:
                nums[idx] = num
                idx += 1
        
        while idx < len(nums):
            nums[idx] = 0
            idx += 1
        