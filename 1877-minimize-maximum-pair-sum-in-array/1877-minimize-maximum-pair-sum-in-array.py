class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort() 
        n=len(nums)-1
        return max([nums[i]+nums[n-i] for i in range(len(nums)//2)])
        