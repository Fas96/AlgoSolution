class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        if len(set(nums))==1:
            return 0 if list(set(nums))[0]==0 else n-1
        
        zeros=0
        randStartZeros=0
        ans=0
        for i in range(n):
            if nums[i]==0:
                zeros+=1
            while zeros>1:
                if nums[randStartZeros]==0:
                    zeros-=1
                randStartZeros+=1
            ans=max(ans,i-randStartZeros) 
        return ans 