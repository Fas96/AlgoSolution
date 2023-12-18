class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        ft=nums[:2]
        lt=nums[n-2:] 
        return (lt[0]*lt[1])-(ft[0]*ft[1])