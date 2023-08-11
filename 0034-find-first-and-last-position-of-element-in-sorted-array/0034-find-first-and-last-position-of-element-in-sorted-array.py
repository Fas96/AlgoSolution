class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bs(nms,t):
            l,r=0,len(nms)
            
            while l< r:
                m=l+((r-l)//2) 
                if nms[m]<t:
                    l = (m+1)
                else:
                    r = m
            return l
                    
        ll=bs(nums,target)
        if ll==len(nums) or nums[ll]!=target:
            return [-1,-1]
        rr=bs(nums,target+1)
        return [ll,rr-1]
            
        