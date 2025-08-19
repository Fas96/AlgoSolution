class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        if not 0 in nums:
            return 0
        ans=0
       
        i=0
        while i<len(nums):
            if nums[i]==0:
                r=i
                while r+1<len(nums) and nums[r+1]==0:
                    r+=1 
                ans+=((r-i+1)*(r-i+1+1)//2)
                i=r+1
            else:
                i+=1
            
       
        return ans
        