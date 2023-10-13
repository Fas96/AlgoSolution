class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        def canform(grades,rd):
            return rd*(rd+1)/2 <= len(grades)
            
        l ,r=0,10**5 
        
        while l<=r:
            m=(l+r)//2
            if canform(grades,m):
                l=m+1 
            else:
                r=m-1
        return r
    
        