class Solution:
    def maxArea(self, height: List[int]) -> int:
        mxAr=0
        l,r=0,len(height)-1
        
        while l<r:
            H=min(height[l],height[r])
            mxAr=max(mxAr,H*(r-l))
            while height[l]<=H and  l<r :
                l+=1 
            while  height[r]<=H and  l<r :
                r-=1 
        return mxAr
        