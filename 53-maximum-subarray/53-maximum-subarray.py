class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax,globalmax=0,0
        
        globalmax=nums[0]
        
        for i in range(len(nums)):
            localMax= max(localMax+nums[i],nums[i])
            globalmax= max(globalmax,localMax)
        return (globalmax)