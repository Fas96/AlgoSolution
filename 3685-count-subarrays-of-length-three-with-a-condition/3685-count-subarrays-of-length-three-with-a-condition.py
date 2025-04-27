class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
         
        return sum(l+r==m/2 for l,m,r in zip(nums,nums[1:],nums[2:]))