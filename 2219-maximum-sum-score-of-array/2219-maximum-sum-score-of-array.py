class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        ans=float('-inf')
        l,r=0,sum(nums)
        
        for i,n in enumerate(nums): 
            ans=max(ans,r,max(ans,l+n))
            l+=n
            r-=n
        
        
        
        return ans
        