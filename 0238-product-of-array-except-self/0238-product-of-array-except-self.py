class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pf=[1]+list(accumulate(nums, operator.mul))
        n=len(nums)
        sf=[1]*n
        for i in range(n-2,-1,-1):
            sf[i]=sf[i+1]*nums[i+1]
        
        ans=[]
        for i in range(len(sf)):
            ans.append(pf[i]*sf[i])
        return ans

        
        