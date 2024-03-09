class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums)>=3 and len(set(nums))==1:
            return sum(nums)
        snums=sorted(nums)
        
        pf=snums[0]+snums[1]
        ans=-1
        for i in range(2,len(snums)):
            if pf>snums[i]:
                ans=pf+snums[i]
            pf+=snums[i]
        return ans
        
        
        