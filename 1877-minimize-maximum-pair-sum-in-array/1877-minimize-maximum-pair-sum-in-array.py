class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        ans=0
        n=len(nums)-1
        
        for i in range(len(nums)//2):
            ans=max(ans,nums[i]+nums[n-i])
        
        return ans
        