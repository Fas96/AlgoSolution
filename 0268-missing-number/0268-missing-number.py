class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # XOR 
        return sum([idx for idx in range(len(nums) + 1)])-sum(nums)
        