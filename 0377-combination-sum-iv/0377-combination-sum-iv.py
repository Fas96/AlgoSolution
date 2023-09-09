class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        c={}
        c[0]=[1]
        def go(t): 
            if t in c:
                return c[t]
            ans=0
            for val in nums:
                if t>val:
                    ans+=go(t-val)
                elif t==val:
                    ans+=1
            c[t]=ans
            return ans
            
             
        return go(target)
        
        
        