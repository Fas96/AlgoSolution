class Solution:
    def singleNumber(self, nums: List[int]) -> int:  
        a = sum(nums) - 3*sum(set(nums))
        return (-a)//2
        