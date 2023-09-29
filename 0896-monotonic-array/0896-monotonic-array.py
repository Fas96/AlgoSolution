class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        N=len(nums)
        if N<2: return True
        stk=[]
        
        for x in nums:
            while stk and stk[-1]>x:
                stk.pop()
            stk.append(x)
        if len(stk)==N:
            return True
        dc=[] 
        for x in nums:
            while dc and dc[-1]<x:
                dc.pop()
            dc.append(x)
        if len(dc)==N:
            return True
        return False
        
        