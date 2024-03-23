class Solution:
    def maxArea(self, height: List[int]) -> int:
        mxAr=0
        l,r=0,len(height)-1
        
        while l<r:
            H=min(height[l],height[r])
            mxAr=max(mxAr,H*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            
        return mxAr
        