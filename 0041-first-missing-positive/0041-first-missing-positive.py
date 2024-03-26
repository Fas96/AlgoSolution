class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
         
        i = 0
        
        while i < n: 
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i]= nums[i], nums[nums[i] - 1]
            else:
                i += 1
        
         
        for i,num in enumerate(nums):
            if num != i + 1: return i + 1 
        return n + 1
            