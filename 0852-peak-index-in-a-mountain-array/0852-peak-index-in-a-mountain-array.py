class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left,right=0,len(arr)-1
        while left<right:
            m1=left+(right-left)//3
            m2=right-((right-left)//3)
            if arr[m1]<arr[m2]:
                left=m1+1
            else:
                right=m2-1
        return left 
         