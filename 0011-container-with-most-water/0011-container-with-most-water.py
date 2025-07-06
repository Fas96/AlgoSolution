class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        ans=-1
        while left<=right:
            breadth=min(height[left],height[right])
            ans=max(ans,breadth*(right-left))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans
        