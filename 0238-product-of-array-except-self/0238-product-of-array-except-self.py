class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pf=[1]+list(accumulate(nums, operator.mul))
        sf=list(accumulate([1]+nums[::-1], operator.mul))[::-1] 
        ans=[]
        sf=sf[1:]
        pf=pf[:-1]
        for i in range(len(pf)):
            ans.append(pf[i]*sf[i])
        return ans

        
        