class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pf=[1]+list(accumulate(nums,operator.mul))
        ans=pf
        print(pf)
        sf=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]=ans[i]*sf
            sf*=nums[i]
        
        
        return ans[:-1]